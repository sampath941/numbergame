import pandas as pd
from itertools import combinations
from collections import Counter

def find_most_frequent_pair(df):
    """Find the most frequent pair of numbers in the DataFrame."""
    unique_numbers = pd.unique(df.values.ravel('K'))
    unique_numbers = sorted(unique_numbers)  # Sort numbers to ensure pairs are generated in a consistent order

    # Generate all unique pairs of numbers
    pairs = list(combinations(unique_numbers, 2))

    # Count occurrences of each pair
    pair_counts = Counter()
    for _, row in df.iterrows():
        row_values = row.dropna().astype(int).tolist()  # Convert row to a list of integers, ignoring NaNs
        for pair in pairs:
            if pair[0] in row_values and pair[1] in row_values:
                pair_counts[pair] += 1

    # Find the most frequent pair
    most_frequent_pair = pair_counts.most_common(1)  # Get the most common pair
    if most_frequent_pair:
        return most_frequent_pair[0]
    return None
