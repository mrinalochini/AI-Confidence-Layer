import json
import streamlit as st
from openai import OpenAI


def generate_claims(question):

    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )

    prompt = f"""
You are an AI answer decomposition system.

Answer the user's question by breaking the answer into
individual factual claims.

Question:
{question}

Return ONLY valid JSON in this exact format:

{{
    "question": "{question}",
    "claims": [
        {{
            "id": 1,
            "text": "First factual claim."
        }},
        {{
            "id": 2,
            "text": "Second factual claim."
        }}
    ]
}}

Rules:
- Each claim should contain one main factual assertion.
- Do not include confidence scores.
- Do not include explanations.
- Do not include markdown.
- Return only JSON.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=False
    )

    answer = response.choices[0].message.content

    return json.loads(answer)
