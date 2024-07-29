import pandas as pd

def count_in_range(row, min_val, max_val, min_count):
    """Check if a row contains at least `min_count` numbers in a given range."""
    return sum(min_val <= x <= max_val for x in row) >= min_count

def count_rows_in_ranges(df):
    """Count rows with specific numbers of values in various ranges."""
    counts = {}
    for count in [2, 3, 4]:
        for min_val, max_val in [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60)]:
            counts[f'count_{count}_{min_val}_to_{max_val}'] = df.apply(count_in_range, axis=1, min_val=min_val, max_val=max_val, min_count=count).sum()
    return counts
