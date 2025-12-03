import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_loader import load_data, clean_data
from analytics import calculate_kpis, calculate_derived_metrics, get_daily_trends
from visualization import generate_charts
from insights import generate_executive_summary
from report_generator import build_pdf
from ml_model_optional import train_model, load_model, save_model, predict_performance
from llm_insights import generate_llm_insights
from dotenv import load_dotenv
load_dotenv()


def main():
    print("Starting AdTech Analytics Pipeline...")
    
    # Configuration
    data_path = "data/ad_data.csv"
    """training_data_path = "data/public_training_data.csv"
    """
    output_dir = "output"
    report_path = os.path.join(output_dir, "adtech_report.pdf")
    
    
    
    # 1. Data Ingestion & Cleaning
    print("1. Loading and cleaning data...")
    try:
        df = load_data(data_path)
        df = clean_data(df)
    except Exception as e:
        print(f"Error in data processing: {e}")
        return

    # 2. Analytics & KPI Calculation
    print("2. Calculating KPIs and trends...")
    kpis = calculate_kpis(df)
    kpis = calculate_derived_metrics(kpis)
    trends = get_daily_trends(df)
    
    
    # 3. Visualization
    print("3. Generating charts...")
    chart_paths = generate_charts(trends, output_dir)
    
    # 4. Insights Generation (LLM + fallback)
    print("4. Generating insights...")
    try:
        summary = generate_llm_insights(kpis, trends)
    except Exception as e:
        print("LLM insights generation failed, falling back to rule-based insights.")
        print("Error:", e)
        summary = generate_executive_summary(kpis, trends)
    
    # 5. Report Generation
    print("5. Building PDF report...")
    build_pdf(kpis, trends, chart_paths, summary, report_path)
    
    print(f"Pipeline completed successfully! Report saved to: {report_path}")


if __name__ == "__main__":
    main()
