from openai import OpenAI
import pandas as pd

client = OpenAI()

def ask_housing_llm(question: str, df: pd.DataFrame):

    # reduce dataset for prompt
    sample = df[["RegionName", "StateName", "Rent", "rent_change_pct"]].head(20)

    prompt = f"""
You are a housing market expert.

A user asked this question about the housing market:

Question:
{question}

Here is some housing data:
{sample.to_string(index=False)}

Answer the question clearly and simply for a general audience.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert real estate analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
