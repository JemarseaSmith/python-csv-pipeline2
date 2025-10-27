#!/usr/bin/env python3
"""
main.py
CLI entrypoint for the python-csv-pipeline starter project.
"""
import argparse
import json
from pipeline import summarize_csv


def parse_args():
    p = argparse.ArgumentParser(
        description="CSV → JSON data pipeline (starter)")
    p.add_argument("input", help="Input CSV file path")
    p.add_argument("--json", help="Write JSON summary to this file")
    p.add_argument("--summary", action="store_true",
                   help="Print summary to stdout")
    return p.parse_args()


def main():
    args = parse_args()
    summary = summarize_csv(args.input)
    if args.summary:
        print(json.dumps(summary, indent=2))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
