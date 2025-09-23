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
