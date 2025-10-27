# pipeline.py
from typing import Dict, Any
import csv


def _try_float(val: str):
    """Return float(val) or raise ValueError."""
    return float(val)


def summarize_csv(path: str) -> Dict[str, Any]:
    """
    Read CSV and compute count, sum, mean for numeric columns.
    Non-numeric values are counted in "non_numeric" field and ignored for numeric stats.
    Returns a dictionary mapping column -> stats dict.
    """
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        numeric_cols = {}        # col -> (sum, count)
        non_numeric = {}         # col -> count of non-numeric or empty values
        # Track columns so columns with only non-numeric values still appear
        seen_columns = []

        for row in reader:
            # Save column order / names
            if not seen_columns:
                seen_columns = list(row.keys())

            for col, val in row.items():
                if val is None or val.strip() == "":
                    non_numeric.setdefault(col, 0)
                    non_numeric[col] += 1
                    continue
                try:
                    x = _try_float(val)
                    s, n = numeric_cols.get(col, (0.0, 0))
                    numeric_cols[col] = (s + x, n + 1)
                except ValueError:
                    non_numeric.setdefault(col, 0)
                    non_numeric[col] += 1

        result = {}
        for col in seen_columns:
            # numeric stats if present
            if col in numeric_cols:
                s, n = numeric_cols[col]
                result[col] = {
                    "count": n,
                    "sum": s,
                    "mean": (s / n) if n > 0 else None
                }
            else:
                result[col] = {}

            # add non-numeric count if any
            if col in non_numeric:
                result[col].setdefault("non_numeric", 0)
                result[col]["non_numeric"] = non_numeric[col]

        return result
