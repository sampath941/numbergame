import pandas as pd

def load_data(filepath):
    """Load data from an Excel file."""
    return pd.read_excel(filepath, usecols="B,C,D,E,F")

def find_duplicates(df):
    """Find and return duplicate rows."""
    return df[df.duplicated()]
