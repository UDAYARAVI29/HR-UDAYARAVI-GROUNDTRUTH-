import pandas as pd
import os

def load_data(filepath):
    """
    Loads data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {e}")

def clean_data(df):
    """
    Cleans and preprocesses the data.
    
    Args:
        df (pd.DataFrame): Raw DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Ensure date column is datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
    
    # Fill missing numeric values with 0
    numeric_cols = ['impressions', 'clicks', 'cost', 'conversions', 'revenue']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)
            
    return df

if __name__ == "__main__":
    # Test the loader
    try:
        df = load_data("data/sample_ad_data.csv")
        clean_df = clean_data(df)
        print(clean_df.head())
        print(clean_df.info())
    except Exception as e:
        print(e)
