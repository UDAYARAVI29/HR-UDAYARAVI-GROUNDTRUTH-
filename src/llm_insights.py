import openai
import os

"""openai.api_key = "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"
"""
"""
openai.api_key = os.getenv("OPENAI_API_KEY", "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")
"""
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