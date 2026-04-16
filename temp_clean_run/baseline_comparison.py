#!/usr/bin/env python3
"""
Baseline comparison: 3 baselines + 2 systems on Dataset B (37 papers).

Baseline 1 (ID match): arXiv ID exists? Yes/No.
Baseline 2 (metadata match): title + first author exact match via arXiv API.
Baseline 3 (fuzzy match): title Jaccard similarity only.

Compared against:
- System A: research-system Level 1 results (from CSV)
- System B: verify_papers.py results (from run output)

Dependencies: pip install pyyaml requests
"""

import csv
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import requests
    import yaml
except ImportError:
    print("pip install pyyaml requests")
    sys.exit(1)

ARXIV_API = "http://export.arxiv.org/api/query?id_list={}"
RATE_LIMIT = 3.5  # seconds between arXiv API calls


def fetch_arxiv(arxiv_id: str) -> dict | None:
    """Fetch metadata from arXiv API. Returns dict or None."""
    try:
        resp = requests.get(ARXIV_API.format(arxiv_id), timeout=15)
        if resp.status_code != 200:
            return None
        root = ET.fromstring(resp.text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return None
        title_el = entry.find("atom:title", ns)
        if title_el is None or title_el.text is None:
            return None
        title = " ".join(title_el.text.strip().split())
        # Check for "Error" entries (paper doesn't exist)
        if title.startswith("Error"):
            return None
        authors = []
        for author in entry.findall("atom:author", ns):
            name = author.find("atom:name", ns)
            if name is not None and name.text:
                authors.append(name.text.strip())
        return {"title": title, "authors": authors, "exists": True}
    except Exception:
        return None


def jaccard_similarity(a: str, b: str) -> float:
    """Word-level Jaccard similarity."""
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def first_author_last_name(name: str) -> str:
    """Extract last name from author string."""
    name = name.strip().rstrip(".")
    parts = name.split()
    if not parts:
        return ""
    return parts[-1].lower()


def run_baselines(catalog_path: str, rs_csv_path: str):
    """Run 3 baselines on all papers with arXiv IDs."""
    with open(catalog_path) as f:
        data = yaml.safe_load(f)

    # Load research-system L1 results
    rs_results = {}
    with open(rs_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rs_results[row["ID"]] = row

    papers = data["papers"]
    results = []

    for p in papers:
        pid = p["id"]
        arxiv_id = p.get("arxiv_id")
        catalog_title = p.get("title", "")
        catalog_authors = p.get("authors", [])
        catalog_first = catalog_authors[0] if catalog_authors else ""

        row = {
            "id": pid,
            "catalog_title": catalog_title,
            "catalog_first_author": catalog_first,
            "has_arxiv": bool(arxiv_id),
            "b1_id_exists": None,
            "b2_metadata_match": None,
            "b2_title_match": None,
            "b2_author_match": None,
            "b3_jaccard": None,
            "rs_l1_verdict": rs_results.get(pid, {}).get("Verdict", "N/A"),
            "rs_l1_error": rs_results.get(pid, {}).get("Error_Type", ""),
        }

        if not arxiv_id:
            row["b1_id_exists"] = "SKIP"
            row["b2_metadata_match"] = "SKIP"
            row["b3_jaccard"] = "SKIP"
            results.append(row)
            print(f"  [{pid}] SKIP (no arXiv ID)")
            continue

        print(f"  [{pid}] Fetching arXiv:{arxiv_id}...", end=" ", flush=True)
        arxiv_data = fetch_arxiv(arxiv_id)
        time.sleep(RATE_LIMIT)

        if arxiv_data is None:
            row["b1_id_exists"] = "NOT_FOUND"
            row["b2_metadata_match"] = "NOT_FOUND"
            row["b3_jaccard"] = 0.0
            print("NOT FOUND")
        else:
            actual_title = arxiv_data["title"]
            actual_authors = arxiv_data["authors"]
            actual_first = actual_authors[0] if actual_authors else ""

            # Baseline 1: ID exists
            row["b1_id_exists"] = "EXISTS"

            # Baseline 2: exact metadata match
            title_exact = catalog_title.lower().strip() == actual_title.lower().strip()
            author_match = (
                first_author_last_name(catalog_first)
                == first_author_last_name(actual_first)
            )
            row["b2_title_match"] = title_exact
            row["b2_author_match"] = author_match
            row["b2_metadata_match"] = "MATCH" if (title_exact and author_match) else "MISMATCH"

            # Baseline 3: Jaccard similarity
            jac = jaccard_similarity(catalog_title, actual_title)
            row["b3_jaccard"] = round(jac, 3)

            print(f"B1=EXISTS B2={'M' if row['b2_metadata_match']=='MATCH' else 'X'} B3={jac:.2f}")

        results.append(row)

    return results


def analyze_failure_regimes(results: list):
    """Identify where baselines are sufficient vs where systems are needed."""
    print("\n" + "=" * 60)
    print("FAILURE REGIME ANALYSIS")
    print("=" * 60)

    # Papers where baselines caught the error
    baseline_sufficient = []
    # Papers where only systems caught the error
    system_needed = []
    # Papers where nothing was checkable
    uncoverable = []

    for r in results:
        has_error = r["rs_l1_verdict"] in ("FAIL", "PARTIAL")
        if not has_error:
            continue

        if r["has_arxiv"] is False or r["b1_id_exists"] == "SKIP":
            uncoverable.append(r)
        elif r["b1_id_exists"] == "NOT_FOUND":
            baseline_sufficient.append(r)
        elif r["b2_metadata_match"] == "MISMATCH" or (r["b3_jaccard"] is not None and r["b3_jaccard"] < 0.5):
            baseline_sufficient.append(r)
        else:
            system_needed.append(r)

    print(f"\nErrors found by RS L1: {sum(1 for r in results if r['rs_l1_verdict'] in ('FAIL','PARTIAL'))}")
    print(f"  Catchable by baseline: {len(baseline_sufficient)}")
    print(f"  Requires staged system: {len(system_needed)}")
    print(f"  Not coverable by API: {len(uncoverable)}")

    if baseline_sufficient:
        print("\n  Baseline-sufficient errors:")
        for r in baseline_sufficient:
            print(f"    [{r['id']}] {r['rs_l1_error']} — B1={r['b1_id_exists']} B2={r['b2_metadata_match']} B3={r['b3_jaccard']}")

    if system_needed:
        print("\n  System-required errors (baseline missed):")
        for r in system_needed:
            print(f"    [{r['id']}] {r['rs_l1_error']} — B1={r['b1_id_exists']} B2={r['b2_metadata_match']} B3={r['b3_jaccard']}")

    if uncoverable:
        print("\n  Not coverable by API (no arXiv ID):")
        for r in uncoverable:
            print(f"    [{r['id']}] {r['rs_l1_error']}")

    return baseline_sufficient, system_needed, uncoverable


if __name__ == "__main__":
    catalog = sys.argv[1] if len(sys.argv) > 1 else "papers_clean_B.yaml"
    rs_csv = sys.argv[2] if len(sys.argv) > 2 else "../04_pilots/pilot_meta_architect_L1_results.csv"

    print(f"Running baselines on {catalog}...")
    results = run_baselines(catalog, rs_csv)
    bs, sn, uc = analyze_failure_regimes(results)

    # Write CSV
    out_csv = catalog.replace(".yaml", "_baseline_results.csv")
    with open(out_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\nResults written to {out_csv}")
