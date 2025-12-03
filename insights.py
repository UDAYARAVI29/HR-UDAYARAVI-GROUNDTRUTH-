def generate_executive_summary(kpis, trends):
    """
    Generates a rule-based executive summary.
    
    Args:
        kpis (dict): Aggregate KPIs.
        trends (pd.DataFrame): Daily trends.
        
    Returns:
        str: Executive summary text.
    """
    
    total_impressions = kpis.get('total_impressions', 0)
    ctr = kpis.get('ctr', 0)
    roas = kpis.get('roas', 0)
    revenue = kpis.get('total_revenue', 0)
    
    summary = []
    
    # Overview
    summary.append(f"During the reporting period, the campaign generated a total of {total_impressions:,} impressions and ${revenue:,.2f} in revenue.")
    
    # Performance Analysis
    if ctr > 1.5:
        summary.append(f"The Click-Through Rate (CTR) was strong at {ctr:.2f}%, indicating high user engagement.")
    elif ctr > 1.0:
        summary.append(f"The Click-Through Rate (CTR) was moderate at {ctr:.2f}%.")
    else:
        summary.append(f"The Click-Through Rate (CTR) was low at {ctr:.2f}%, suggesting a need for creative optimization.")
        
    if roas > 2.0:
        summary.append(f"Return on Ad Spend (ROAS) was excellent at {roas:.2f}, showing high profitability.")
    elif roas > 1.0:
        summary.append(f"Return on Ad Spend (ROAS) was positive at {roas:.2f}.")
    else:
        summary.append(f"Return on Ad Spend (ROAS) was {roas:.2f}, indicating spend inefficiency.")
        
    # Trend Analysis
    start_revenue = trends.iloc[0]['revenue']
    end_revenue = trends.iloc[-1]['revenue']
    
    if end_revenue > start_revenue:
        summary.append("Revenue showed an upward trend towards the end of the period.")
    else:
        summary.append("Revenue trended downwards or remained flat towards the end of the period.")
        
    return "\n".join(summary)

if __name__ == "__main__":
    # Test insights
    try:
        from data_loader import load_data, clean_data
        from analytics import calculate_kpis, calculate_derived_metrics, get_daily_trends
        
        df = load_data("data/sample_ad_data.csv")
        df = clean_data(df)
        kpis = calculate_kpis(df)
        kpis = calculate_derived_metrics(kpis)
        trends = get_daily_trends(df)
        
        summary = generate_executive_summary(kpis, trends)
        print(summary)
    except Exception as e:
        print(e)
