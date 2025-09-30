#!/usr/bin/env python3
"""
Assignment 3/4: Best Practices + Testing

- Uses argparse with flags: --country, --country_column, --fires_column, --file_name
- Optional --op to compute mean/median/stdev on the values
- Uses a main() entry point
- Exit codes: 0 on success; 1 if no matching rows; 2 on errors
"""

import argparse
import sys

from my_utils import get_column, mean, median, stdev  # added imports


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Compute fires stats for a country from a CSV"
    )
    p.add_argument("--country", required=True, help="Exact country name to match")
    p.add_argument(
        "--country_column",
        type=int,
        required=True,
        help="Zero-based index of the country column",
    )
    p.add_argument(
        "--fires_column",
        type=int,
        required=True,
        help="Zero-based index of the fires column",
    )
    p.add_argument("--file_name", required=True, help="Path to CSV file")
    p.add_argument(
        "--op",
        choices=["mean", "median", "stdev"],
        help="Optional operation to apply; if omitted, prints sum(values)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    try:
        values = get_column(
            file_name=args.file_name,
            query_column=args.country_column,
            query_value=args.country,
            result_column=args.fires_column,
        )
        if not values:
            print(f"No rows found for country={args.country!r}", file=sys.stderr)
            sys.exit(1)

        if args.op == "mean":
            print(mean(values))
        elif args.op == "median":
            print(median(values))
        elif args.op == "stdev":
            print(stdev(values))  # requires at least 2 values
        else:
            total = sum(values)
            print(total)

        sys.exit(0)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
