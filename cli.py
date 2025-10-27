"""Small CLI entrypoint to run the pipeline.

Usage examples:
  python -m cli -i data/input.csv -o data/output.csv
  python cli.py --input data/input.csv --output data/output.csv

This script tries to import the pipeline module and call a runnable function
in this order: run(input, output), run_pipeline(input, output), main().
If the pipeline function accepts no args it will be called without args.
"""

from importlib import import_module
import argparse
import sys


def find_pipeline_callable(module):
    for name in ("run", "run_pipeline", "main"):
        if hasattr(module, name):
            return getattr(module, name)
    return None


def call_pipeline(func, input_path, output_path):
    # Try calling with (input, output), then with no args as a fallback
    try:
        return func(input_path, output_path)
    except TypeError:
        return func()


def main():
    parser = argparse.ArgumentParser(description="Run the CSV pipeline.")
    parser.add_argument("-i", "--input", required=True, help="Input CSV file path")
    parser.add_argument(
        "-o", "--output", default="output.csv", help="Output CSV file path"
    )
    args = parser.parse_args()

    try:
        pipeline = import_module("pipeline")
    except Exception as e:
        print("Error: could not import pipeline module:", e, file=sys.stderr)
        sys.exit(2)

    func = find_pipeline_callable(pipeline)
    if func is None:
        print(
            "Error: no runnable function found in pipeline.py. "
            "Define run(input, output) or run_pipeline(input, output) or main().",
            file=sys.stderr,
        )
        sys.exit(3)

    try:
        call_pipeline(func, args.input, args.output)
    except Exception as e:
        print("Pipeline execution failed:", e, file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
