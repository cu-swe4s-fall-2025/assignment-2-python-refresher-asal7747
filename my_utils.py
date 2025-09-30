import csv


def get_column(file_name, query_column, query_value, result_column=1):
    """
    Return a list of integers from result_column for rows where
    row[query_column] == query_value.

    - Skips the header row
    - Raises FileNotFoundError if the file is missing
    - Raises ValueError if a matched cell is not numeric
    - Raises IndexError if given column indexes are negative
    """
    if query_column < 0 or result_column < 0:
        raise IndexError("query_column and result_column must be >= 0")

    out = []
    with open(file_name, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return out

    data = rows[1:]  # Skip header row
    # start=2 so row numbers match file lines
    for i, row in enumerate(data, start=2):
        if query_column >= len(row) or result_column >= len(row):
            # If a particular row is short, just skip it
            continue
        if row[query_column].strip() == query_value:
            cell = row[result_column].strip()
            if cell == "":
                raise ValueError(
                    f"Row {i}: expected number at col {result_column}, got empty"
                )
            try:
                # Accept ints or decimals (e.g., "0.0"); still return int list
                value = int(float(cell))
            except ValueError as e:
                raise ValueError(
                    f"Row {i}: expected number at col {result_column}, got {cell!r}"
                ) from e
            out.append(value)
    return out


def mean(values: list[int]) -> float:
    """
    Return the arithmetic mean of a non-empty list of integers.
    Raises ValueError for an empty list.
    """
    if not values:
        raise ValueError("mean() requires a non-empty list")
    return sum(values) / len(values)


def median(values: list[int]) -> float:
    """
    Return the median of a non-empty list of integers.
    For even length, return the average of the two middle values as float.
    Raises ValueError for an empty list.
    """
    n = len(values)
    if n == 0:
        raise ValueError("median() requires a non-empty list")
    s = sorted(values)
    mid = n // 2
    if n % 2 == 1:
        return float(s[mid])
    return (s[mid - 1] + s[mid]) / 2.0


def stdev(values: list[int]) -> float:
    """
    Return the sample standard deviation with Bessel's correction.
    Requires at least two values; raises ValueError otherwise.
    s = sqrt( sum((x - mean)^2) / (n - 1) )
    """
    n = len(values)
    if n < 2:
        raise ValueError("stdev() requires at least two values")
    m = mean(values)
    ss = sum((x - m) ** 2 for x in values)
    return (ss / (n - 1)) ** 0.5
