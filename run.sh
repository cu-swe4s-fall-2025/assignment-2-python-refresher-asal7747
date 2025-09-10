#!/usr/bin/env bash
# Purpose: Run print_fires.py to compute TOTAL CO2 from fire-related categories
# for a given country using the Agrofood_co2_emission.csv dataset.
python3 print_fires.py --file "data/Agrofood_co2_emission.csv" --country "Liechtenstein" --country-col 1 --fire-cols 3 4 23 24
