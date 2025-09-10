[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)

# Python Refresher - Assignment 2

## Overview

This repository contains a small Python refresher assignment that reads an agricultural CO₂ dataset and prints a single number computed for a selected country.

The script `print_fires.py` uses a helper function `get_column()` to filter rows by country and collect values before summing selected fire-related CO₂ columns. Column numbers are provided as 1-based indices to match the CSV header, then converted to 0-based internally.

## Data

Place `Agrofood_co2_emission.csv` in the `data/` directory as `data/Agrofood_co2_emission.csv`.

## Usage

Run with the helper script:

```bash
./run.sh
```

## Notes

- `print_fires.py` uses `argparse` for flags like `--country` and `--fire-cols`.
- It accepts 1-based column numbers to match the CSV header and converts them to 0-based internally before calling `get_column()`.