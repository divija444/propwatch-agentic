from openai import OpenAI
import pandas as pd

client = OpenAI()

def generate_market_insights(df: pd.DataFrame):

    # take small sample for prompt
    sample = df[["RegionName", "Rent", "rent_change_pct"]].head(10)

    prompt = f"""
You are a real estate market analyst.

Analyze the housing market data below and summarize insights.

Data:
{sample.to_string(index=False)}

Explain:
1. Cities with strongest rent growth
2. Any trends you notice
3. Possible investment opportunities

Keep the explanation simple.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional housing market analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
