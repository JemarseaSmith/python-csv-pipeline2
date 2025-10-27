```markdown
# python-csv-pipeline

Small CLI tool that reads CSV files, validates and summarizes numeric columns, and can output JSON.

Features
- Read CSV from a file.
- Compute basic stats (count, sum, mean) per numeric column.
- Report counts of non-numeric / missing values per column.
- Simple CLI with argparse.
- Unit tests with pytest and a GitHub Actions CI workflow.

Quick start (Windows PowerShell)
1. Clone repo (after you push it to your GitHub):
   - git clone https://github.com/JemarseaSmith/python-csv-pipeline.git
   - cd python-csv-pipeline

2. Create and activate venv:
   - py -3 -m venv .venv
   - .\.venv\Scripts\Activate.ps1

3. Install test dependency:
   - pip install --upgrade pip
   - pip install pytest

4. Run tests:
   - pytest -q

5. Run the CLI:
   - python main.py examples/sample.csv --summary
   - python main.py examples/sample.csv --json output.json

Project layout
- main.py       # CLI entrypoint
- pipeline.py   # core parsing and summary functions
- tests/        # unit tests
- .github/workflows/python-app.yml  # CI to run pytest
- README.md, LICENSE, .gitignore

Notes
- This is a small starter project meant to be extended. You can:
  - Add command-line options (skip columns, select columns).
  - Add more statistics (median, stddev).
  - Add streaming support for large CSVs.
  - Add a small demo GIF or output sample to the README.
```
