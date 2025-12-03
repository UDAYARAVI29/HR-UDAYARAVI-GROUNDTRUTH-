from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime

def build_pdf(kpis, trends, chart_paths, summary, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # ---------------------------------------
    # Custom Styles
    # ---------------------------------------
    styles.add(ParagraphStyle(
        name='Justify',
        parent=styles['Normal'],
        alignment=4,  # Justify
        fontSize=10,
        leading=14
    ))

    styles.add(ParagraphStyle(
        name='Heading',
        parent=styles['Heading2'],
        spaceAfter=4,
        spaceBefore=6
    ))

    story = []

    # ---------------------------------------
    # TITLE
    # ---------------------------------------
    story.append(Paragraph("AdTech Performance Report", styles['Title']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1, 12))

    # ---------------------------------------
    # EXECUTIVE SUMMARY
    # ---------------------------------------
    story.append(Paragraph("Executive Summary", styles['Heading']))
    story.append(Spacer(1, 4))

    clean_summary = summary.replace("**", "")
    for line in clean_summary.split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), styles['Justify']))
            story.append(Spacer(1, 4))

    story.append(Spacer(1, 12))

    # ---------------------------------------
    # KPI TABLE
    # ---------------------------------------
    story.append(Paragraph("Key Performance Indicators (KPIs)", styles['Heading']))
    story.append(Spacer(1, 6))

    kpi_data = [
        ['Metric', 'Value'],
        ['Total Impressions', f"{kpis['total_impressions']:,}"],
        ['Total Clicks', f"{kpis['total_clicks']:,}"],
        ['CTR', f"{kpis['ctr']:.2f}%"],
        ['Total Cost', f"${kpis['total_cost']:,.2f}"],
        ['Total Revenue', f"${kpis['total_revenue']:,.2f}"],
        ['ROAS', f"{kpis['roas']:.2f}"],
        ['Conversions', f"{kpis['total_conversions']:,}"]
    ]

    kpi_table = Table(kpi_data, colWidths=[3.2*inch, 2.2*inch])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))

    story.append(kpi_table)
    story.append(PageBreak())

    # ---------------------------------------
    # CHARTS PAGE 1
    # ---------------------------------------
    story.append(Paragraph("Performance Trends", styles['Heading']))
    story.append(Spacer(1, 8))

    if 'impressions_trend' in chart_paths:
        story.append(Paragraph("Daily Impressions", styles['Heading']))
        story.append(Image(chart_paths['impressions_trend'], width=6*inch, height=3.2*inch))
        story.append(Spacer(1, 10))

    if 'clicks_trend' in chart_paths:
        story.append(Paragraph("Daily Clicks", styles['Heading']))
        story.append(Image(chart_paths['clicks_trend'], width=6*inch, height=3.2*inch))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # ---------------------------------------
    # CHARTS PAGE 2
    # ---------------------------------------
    if 'ctr_trend' in chart_paths:
        story.append(Paragraph("Click-Through Rate (CTR)", styles['Heading']))
        story.append(Image(chart_paths['ctr_trend'], width=6*inch, height=3.2*inch))
        story.append(Spacer(1, 10))

    if 'revenue_trend' in chart_paths:
        story.append(Paragraph("Revenue Trend", styles['Heading']))
        story.append(Image(chart_paths['revenue_trend'], width=6*inch, height=3.2*inch))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # ---------------------------------------
    # DATA APPENDIX
    # ---------------------------------------
    story.append(Paragraph("Data Appendix", styles['Heading']))
    story.append(Spacer(1, 6))

    # Remove time from datetime column
    clean_trends = trends.copy()
    if "date" in clean_trends.columns:
        clean_trends["date"] = clean_trends["date"].dt.strftime("%Y-%m-%d")

    data = [clean_trends.columns.tolist()] + clean_trends.head(20).values.tolist()

    formatted = []
    for row in data:
        r = []
        for item in row:
            r.append(f"{item:.2f}" if isinstance(item, float) else str(item))
        formatted.append(r)

    table = Table(formatted, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.grey)
    ]))

    story.append(table)

    # ---------------------------------------
    # BUILD REPORT
    # ---------------------------------------
    doc.build(story)
    print(f"PDF Report generated at: {output_path}")
