#!/usr/bin/env python3
"""
triage.py — risk-prioritize Nmap findings.

Reads a CSV of host/port/service findings with CVSS base scores and prints a
remediation list ordered by severity. Standard library only; synthetic data.
"""
import argparse
import csv


def sev(cvss):
    if cvss >= 9.0: return "CRITICAL"
    if cvss >= 7.0: return "HIGH"
    if cvss >= 4.0: return "MEDIUM"
    if cvss > 0.0:  return "LOW"
    return "INFO"


def main():
    p = argparse.ArgumentParser(description="Prioritize Nmap findings by CVSS.")
    p.add_argument("findings_csv")
    args = p.parse_args()

    rows = []
    with open(args.findings_csv, newline="") as f:
        for r in csv.DictReader(f):
            r["cvss"] = float(r["cvss"])
            r["sev"] = sev(r["cvss"])
            rows.append(r)
    rows.sort(key=lambda r: r["cvss"], reverse=True)

    print(f"{'CVSS':>5}  {'SEV':9} {'HOST':16} {'PORT':5} FINDING")
    print("-" * 78)
    for r in rows:
        print(f"{r['cvss']:>5}  {r['sev']:9} {r['host']:16} {r['port']:5} {r['finding']}")
    actionable = [r for r in rows if r["sev"] in ("CRITICAL", "HIGH")]
    print("-" * 78)
    print(f"{len(rows)} findings | {len(actionable)} HIGH/CRITICAL to remediate first")


if __name__ == "__main__":
    main()
