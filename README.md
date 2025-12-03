#   H-001 The Automated Insight Engine -- Automated AdTech Analytics Pipeline with AI Prediction

##  Project Overview
This project is a fully automated **Data Engineering & Analytics System** designed for the AdTech industry. It ingests raw advertising performance data, processes it to calculate key metrics (KPIs), generates trend visualizations, and uses **Machine Learning** to predict future performance.

The final output is a professional, executive-ready **PDF Report** generated automatically, requiring zero manual intervention.

##  Key Features
- **Automated Data Ingestion**: Loads and cleans raw CSV data.
- **Advanced Analytics**: Calculates Impressions, Clicks, CTR, CPC, ROAS, and Revenue.
- **AI-Powered Predictions**: Uses a Random Forest model to predict Click-Through Rates (CTR) based on historical data.
- **Dynamic Visualization**: Generates trend charts for Impressions, Clicks, CTR, and Revenue.
- **Executive Reporting**: Assembles all insights, charts, and AI predictions into a polished PDF report.
- **Creates AI-powered natural-language insights using an LLM**

##  Tech Stack
- **Python**: Core logic and orchestration.
- **Pandas**: Data manipulation and KPI calculation.
- **Matplotlib**: Data visualization and charting.
- **Scikit-Learn**: Machine Learning for CTR prediction.
- **ReportLab**: PDF report generation.
-**Machine Learning**: Scikit-Learn (RandomForestRegressor)
-**LLM Integration**:	OpenAI API

##  Quick Start Guide

### 1. Prerequisites
Ensure you have Python installed.

### 2. Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline
Execute the main script to run the full analysis:
```bash
python main.py
```

### 4. View Results
Navigate to the `output/` directory to find your report:
- **`adtech_report.pdf`**: The complete analysis.
- **`*.png`**: Individual chart images.

##  Input Data Format
To analyze your own data, replace `data/sample_ad_data.csv` with a CSV file containing:
- `date`, `impressions`, `clicks`, `cost`, `conversions`, `revenue`, `device`, `country`

##  Machine Learning Model
The system automatically checks for a trained model. If none exists, it instantly trains a new **Random Forest Regressor** using `data/public_training_data.csv` to provide accurate baseline predictions for your report.
