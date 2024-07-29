import pandas as pd

def count_occurrences(df):
    """Count occurrences of numbers in each column."""
    counts = {}
    for column in df.columns:
        count_series = df[column].value_counts().sort_index()
        counts[column] = count_series
    return pd.DataFrame(counts).fillna(0).astype(int)

def add_totals(counts_df):
    """Add totals and sort counts DataFrame."""
    counts_df['Total'] = counts_df.sum(axis=1)
    counts_df2 = counts_df.reset_index().rename(columns={'index': 'Index_df1'})
    counts_df_sort = counts_df.sort_values(by=['Total'], ascending=False)
    counts_df_sort2 = counts_df_sort.reset_index().rename(columns={'index': 'Index_df2'})
    return counts_df2, counts_df_sort2
