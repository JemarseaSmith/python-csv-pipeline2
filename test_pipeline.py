# tests/test_pipeline.py
from pipeline import summarize_csv
import tempfile
import os


def test_summarize_csv_basic(tmp_path):
    csv_content = "a,b\n1,2\n3,4\n"
    p = tmp_path / "data.csv"
    p.write_text(csv_content)
    res = summarize_csv(str(p))
    assert "a" in res and "b" in res
    assert res["a"]["count"] == 2
    assert res["a"]["sum"] == 4.0
    assert res["a"]["mean"] == 2.0


def test_non_numeric_values(tmp_path):
    csv_content = "a,b\n1,hello\n,4\nx,5\n"
    p = tmp_path / "data2.csv"
    p.write_text(csv_content)
    res = summarize_csv(str(p))
    # column a: numeric values: 1 -> count 1, sum 1.0; non-numeric/empty -> 2
    assert res["a"]["count"] == 1
    assert res["a"]["sum"] == 1.0
    assert res["a"]["non_numeric"] == 2
    # column b: numeric values: 4,5 -> count 2
    assert res["b"]["count"] == 2
    assert res["b"]["sum"] == 9.0
