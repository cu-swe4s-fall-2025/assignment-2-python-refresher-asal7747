#!/usr/bin/env bash
set -euo pipefail

# Ensure ssshtest is available, then source it
test -e ssshtest || curl -s -o ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Always run from repo root
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

csv="tests/functional/agro_subset.csv"

# Match original header: country in col 0, fires value in col 2 (0-based)
country_col=0
fires_col=2

# Negative case first: no matching rows -> exit 1 with stderr
set +e  # Temporarily disable exit-on-error for negative test
run no_match_country python3 print_fires.py \
  --country "NoSuchCountry" \
  --country_column "${country_col}" \
  --fires_column "${fires_col}" \
  --file_name "${csv}"
set -e  # Re-enable exit-on-error
assert_stderr
assert_in_stderr "No rows found"
assert_exit_code 1

# 1) Sum default (no --op)
run sum_default python3 print_fires.py \
  --country "Colombia" \
  --country_column "${country_col}" \
  --fires_column "${fires_col}" \
  --file_name "${csv}"
assert_stdout
assert_in_stdout 29188275
assert_no_stderr
assert_exit_code 0

# 2) Mean
run mean_op python3 print_fires.py \
  --country "Colombia" \
  --country_column "${country_col}" \
  --fires_column "${fires_col}" \
  --file_name "${csv}" \
  --op mean
assert_stdout
assert_in_stdout 3648534.375
assert_no_stderr
assert_exit_code 0

# 3) Median
run median_op python3 print_fires.py \
  --country "Colombia" \
  --country_column "${country_col}" \
  --fires_column "${fires_col}" \
  --file_name "${csv}" \
  --op median
assert_stdout
assert_in_stdout 1808.5
assert_no_stderr
assert_exit_code 0

# 4) Stdev (requires at least two values)
run stdev_op python3 print_fires.py \
  --country "Colombia" \
  --country_column "${country_col}" \
  --fires_column "${fires_col}" \
  --file_name "${csv}" \
  --op stdev
assert_stdout
stdev_val="$(echo "$stdev_op_STDOUT" | tr -d '[:space:]')"
python3 - <<'PY'
import math, sys
expected = 10314437.583439313
got = float(sys.argv[1])
# Accept small float error
ok = math.isclose(got, expected, rel_tol=1e-12, abs_tol=1e-9)
print("OK" if ok else f"DIFF got={got} expected={expected}")
sys.exit(0 if ok else 1)
PY
"$stdev_val"
assert_no_stderr
assert_exit_code 0

