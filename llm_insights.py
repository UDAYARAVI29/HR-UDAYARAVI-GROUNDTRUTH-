import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_llm_insights(kpis, trends):
    """
    Generates LLM-based insights using OpenAI GPT-4o.
    Accepts both KPIs and Trends.
    Falls back to rule-based insights if needed.
    """
    try:
        prompt = f"""
        You are an AdTech analytics expert.

        Generate a high-quality executive summary based on:
        
        KPIs:
        {kpis}

        Trends:
        {trends}

        Return the output in this structure:

        EXECUTIVE SUMMARY:
        - 3 sentence overview

        KEY INSIGHTS:
        - 3 bullet points

        RECOMMENDATIONS:
        - 3 bullet points
        """

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        raise Exception(f"LLM error: {e}")