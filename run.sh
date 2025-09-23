#!/usr/bin/env bash
# Assignment 3: one success run + two error demonstrations (simple version)

set -euo pipefail
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"

echo "OK run:"
python3 print_fires.py \
  --country "Liechtenstein" \
  --country_column 0 \
  --fires_column 2 \
  --file_name data/Agrofood_co2_emission.csv || true

echo
echo "Error run (missing file):"
if python3 print_fires.py \
  --country "Liechtenstein" \
  --country_column 0 \
  --fires_column 2 \
  --file_name data/DOES_NOT_EXIST.csv; then
  echo "Unexpected success"; exit 1
else
  echo "Expected failure occurred"
fi

echo
echo "Error run (bad column index):"
if python3 print_fires.py \
  --country "Liechtenstein" \
  --country_column 0 \
  --fires_column 9999 \
  --file_name data/Agrofood_co2_emission.csv; then
  echo "Unexpected success"; exit 1
else
  echo "Expected failure occurred"
fi
