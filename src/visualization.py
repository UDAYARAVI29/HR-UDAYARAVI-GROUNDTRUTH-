import matplotlib.pyplot as plt
import os

def generate_charts(daily_df, output_dir):
    """
    Generates and saves charts based on daily trends.
    
    Args:
        daily_df (pd.DataFrame): DataFrame with daily aggregated metrics.
        output_dir (str): Directory to save the charts.
        
    Returns:
        dict: Dictionary mapping chart names to their file paths.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    chart_paths = {}
    
    # Common style settings
    plt.style.use('ggplot')
    
    # 1. Impressions Trend
    plt.figure(figsize=(10, 6))
    plt.plot(daily_df['date'], daily_df['impressions'], marker='o', color='b', label='Impressions')
    plt.title('Daily Impressions Trend')
    plt.xlabel('Date')
    plt.ylabel('Impressions')
    plt.grid(True)
    plt.tight_layout()
    impressions_path = os.path.join(output_dir, 'impressions_trend.png')
    plt.savefig(impressions_path)
    plt.close()
    chart_paths['impressions_trend'] = impressions_path
    
    # 2. Clicks Trend
    plt.figure(figsize=(10, 6))
    plt.plot(daily_df['date'], daily_df['clicks'], marker='o', color='g', label='Clicks')
    plt.title('Daily Clicks Trend')
    plt.xlabel('Date')
    plt.ylabel('Clicks')
    plt.grid(True)
    plt.tight_layout()
    clicks_path = os.path.join(output_dir, 'clicks_trend.png')
    plt.savefig(clicks_path)
    plt.close()
    chart_paths['clicks_trend'] = clicks_path
    
    # 3. CTR Trend
    plt.figure(figsize=(10, 6))
    plt.plot(daily_df['date'], daily_df['ctr'], marker='o', color='r', label='CTR (%)')
    plt.title('Daily CTR Trend')
    plt.xlabel('Date')
    plt.ylabel('CTR (%)')
    plt.grid(True)
    plt.tight_layout()
    ctr_path = os.path.join(output_dir, 'ctr_trend.png')
    plt.savefig(ctr_path)
    plt.close()
    chart_paths['ctr_trend'] = ctr_path
    
    # 4. Revenue Trend
    plt.figure(figsize=(10, 6))
    plt.plot(daily_df['date'], daily_df['revenue'], marker='o', color='purple', label='Revenue')
    plt.title('Daily Revenue Trend')
    plt.xlabel('Date')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.tight_layout()
    revenue_path = os.path.join(output_dir, 'revenue_trend.png')
    plt.savefig(revenue_path)
    plt.close()
    chart_paths['revenue_trend'] = revenue_path
    
    print(f"Charts saved to {output_dir}")
    return chart_paths

if __name__ == "__main__":
    # Test visualization
    try:
        from data_loader import load_data, clean_data
        from analytics import get_daily_trends
        
        df = load_data("data/sample_ad_data.csv")
        df = clean_data(df)
        trends = get_daily_trends(df)
        
        generate_charts(trends, "output")
    except Exception as e:
        print(e)
