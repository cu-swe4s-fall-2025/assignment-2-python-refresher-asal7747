# Assignment 3 – Best Practices

## Overview
Command-line tool that sums a fires column for a selected country from a CSV using zero-based column indexes.

## Requirements
- Python 3.8+
- Data file: data/Agrofood_co2_emission.csv

## Usage
```bash
# Show help
python3 print_fires.py --help

# OK example (adjust indices to the CSV if needed)
python3 print_fires.py \
  --country "Liechtenstein" \
  --country_column 0 \
  --fires_column 2 \
  --file_name data/Agrofood_co2_emission.csv
```

## Error examples
```bash
# Missing file
python3 print_fires.py \
  --country "Liechtenstein" \
  --country_column 0 \
  --fires_column 2 \
  --file_name data/DOES_NOT_EXIST.csv

# Bad column index
python3 print_fires.py \
  --country "Liechtenstein" \
  --country_column 0 \
  --fires_column 9999 \
  --file_name data/Agrofood_co2_emission.csv
```

## Exit codes
- 0: success
- 1: no matching rows for the country
- 2: other errors (I/O or value parsing)

## Notes
- Uses argparse and a main() entry point.
- get_column returns a list of integers and accepts numeric strings like "0.0".  

# Assignment 4 – Testing

## Overview
Testing suite for the print_fires.py command-line tool including unit tests for utility functions and functional tests for end-to-end behavior.

## Requirements
- Python 3.8+
- ssshtest framework (automatically downloaded)
- Test data file: tests/functional/agro_subset.csv

## Usage
```bash
# Run unit tests
python3 -m unittest tests/unit/test_myutils.py

# Run functional tests
bash tests/functional/test_printfires.sh
```

## Test Coverage
- **Unit tests**: Test mathematical functions (mean, median, stdev) and CSV parsing
- **Functional tests**: Test CLI interface with various operations and error conditions

## Notes
- Functional tests use ssshtest and a 25-row subset dataset at `tests/functional/agro_subset.csv`
- CLI flags are required: `--country`, `--country_column`, `--fires_column`, `--file_name`
- Optional `--op` selects mean, median, or stdev; if omitted, the script prints the sum of values
- Exit codes: 0 success; 1 no matching rows; 2 other errors (I/O, parsing)
