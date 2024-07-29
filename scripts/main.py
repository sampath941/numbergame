import sys
import os
import pandas as pd
print('The version of pandas installed is:',pd.__version__)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))

from data_preprocessing import load_data, find_duplicates
from count_values import count_occurrences, add_totals
from count_ranges import count_rows_in_ranges
from find_pairs import find_most_frequent_pair



def main():
    # File paths
    data_filepath = 'data/lifeline7.xlsx'

    # Load and preprocess data
    df = load_data(data_filepath)
    duplicate_rows = find_duplicates(df)
    print("Number of duplicateRows:", duplicate_rows.shape[0])
    
    # Count occurrences and process DataFrames
    counts_df = count_occurrences(df)
    counts_df2, counts_df_sort2 = add_totals(counts_df)
    
    # Save combined DataFrame
    blank_df = pd.DataFrame({'Blank_Column': [pd.NA] * 500})
    combined_df = pd.concat([counts_df2, blank_df, counts_df_sort2], ignore_index=False, axis=1, join='outer')
    combined_df.to_csv('tmp/number_counts.csv', index=False)
    
    # Print DataFrames
    print(counts_df2)
    print(counts_df_sort2)
    
    # Count rows in ranges
    range_counts = count_rows_in_ranges(df)
    for key, value in range_counts.items():
        print(f"Number of rows with at least {key.split('_')[1]} numbers between {key.split('_')[2]} and {key.split('_')[4]}: {value}")
    
    # Find most frequent pair
    most_frequent_pair = find_most_frequent_pair(df)
    if most_frequent_pair:
        pair, count = most_frequent_pair
        print(f"The most frequent pair is {pair} with {count} occurrences.")
    else:
        print("No pairs found.")

if __name__ == '__main__':
    main()

