# print_fires.py
# Step 7: sum multiple fire-related CO2 columns for a country.
# This version accepts 1-based column numbers from the user and converts
# to 0-based.

# Uses get_column(result_column=...) with a default available (step 9);
# updated per step 10.


import argparse
from my_utils import get_column


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Sum selected fire-related CO2 columns for a given country "
            "(1-based column inputs)."
        )
    )
    parser.add_argument(
        "--file",
        default="data/Agrofood_co2_emission.csv",
        help=(
            "Path to the CSV file "
            "(default: data/Agrofood_co2_emission.csv)"
        ),
    )
    parser.add_argument(
        "--country",
        default="Liechtenstein",
        help='Country name to match (default: "Liechtenstein")',
    )

    # Treat these as 1-based indices to match the CSV labeling.
    parser.add_argument(
        "--country-col",
        type=int,
        default=1,  # 1-based: first column
        help="1-based index of the country column (default: 1)",
    )

    # 1-based fire-related columns (3, 4, 23, 24).
    parser.add_argument(
        "--fire-cols",
        type=int,
        nargs="+",
        default=[3, 4, 23, 24],
        help=(
            "1-based indices of fire-related CO2 columns to SUM "
            "(default: 3 4 23 24)"
        ),
    )

    args = parser.parse_args()

    # Convert 1-based inputs to 0-based for internal indexing
    query_col_0 = args.country_col - 1
    fire_cols_0 = [c - 1 for c in args.fire_cols]

    grand_total = 0.0
    for col0 in fire_cols_0:
        values = get_column(
            file_name=args.file,
            query_column=query_col_0,
            query_value=args.country,
            # Step 10: use the named argument added in step 9
            result_column=col0,
        )
        for v in values:
            try:
                grand_total += float(v)
            except ValueError:
                continue


    print(grand_total)



if __name__ == "__main__":
    main()


