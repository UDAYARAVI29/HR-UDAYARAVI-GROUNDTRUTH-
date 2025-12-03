import pandas as pd

def calculate_kpis(df):
    """
    Calculates aggregate KPIs from the dataframe.
    
    Args:
        df (pd.DataFrame): Cleaned DataFrame.
        
    Returns:
        dict: Dictionary containing total impressions, clicks, cost, revenue, conversions.
    """
    kpis = {
        'total_impressions': df['impressions'].sum(),
        'total_clicks': df['clicks'].sum(),
        'total_cost': df['cost'].sum(),
        'total_revenue': df['revenue'].sum(),
        'total_conversions': df['conversions'].sum()
    }
    return kpis

def calculate_derived_metrics(kpis):
    """
    Calculates derived metrics like CTR, CPC, ROAS from aggregate KPIs.
    
    Args:
        kpis (dict): Dictionary of aggregate KPIs.
        
    Returns:
        dict: Dictionary with added derived metrics.
    """
    # Avoid division by zero
    impressions = kpis['total_impressions'] if kpis['total_impressions'] > 0 else 1
    clicks = kpis['total_clicks'] if kpis['total_clicks'] > 0 else 1
    cost = kpis['total_cost'] if kpis['total_cost'] > 0 else 1
    
    kpis['ctr'] = (kpis['total_clicks'] / impressions) * 100
    kpis['cpc'] = kpis['total_cost'] / clicks
    kpis['cpm'] = (kpis['total_cost'] / impressions) * 1000
    kpis['roas'] = kpis['total_revenue'] / cost
    
    return kpis

def get_daily_trends(df):
    """
    Aggregates data by date to get daily trends.
    
    Args:
        df (pd.DataFrame): Cleaned DataFrame.
        
    Returns:
        pd.DataFrame: DataFrame with daily aggregated metrics.
    """
    daily_df = df.groupby('date')[['impressions', 'clicks', 'cost', 'revenue', 'conversions']].sum().reset_index()
    
    # Calculate daily derived metrics for plotting
    daily_df['ctr'] = (daily_df['clicks'] / daily_df['impressions']) * 100
    daily_df['roas'] = daily_df['revenue'] / daily_df['cost']
    
    return daily_df

if __name__ == "__main__":
    # Test analytics
    try:
        from data_loader import load_data, clean_data
        df = load_data("data/sample_ad_data.csv")
        df = clean_data(df)
        
        kpis = calculate_kpis(df)
        kpis = calculate_derived_metrics(kpis)
        print("KPIs:", kpis)
        
        trends = get_daily_trends(df)
        print("Trends head:", trends.head())
    except Exception as e:
        print(e)
