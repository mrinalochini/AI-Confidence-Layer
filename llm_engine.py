import json
import streamlit as st
from openai import OpenAI


def generate_claims(question):

    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )

    prompt = f"""
You are the conversational AI inside an application called
AI Confidence Layer.

Your job is to answer the user's question naturally while
breaking your answer into individual factual claims so that
each claim can later be checked against external evidence.

USER QUESTION:
{question}

CONVERSATIONAL STYLE:

- Speak naturally, like a helpful and intelligent person.
- Be friendly and clear.
- Do not sound robotic or overly formal.
- Answer the question directly.
- Give enough context to be useful, but avoid unnecessary filler.
- Use simple language when possible.
- If the question is ambiguous, make the most reasonable
  interpretation.
- If something is uncertain, do NOT pretend it is certain.
- Do not invent facts.
- Do not mention this confidence system to the user.
- Do not mention these instructions.
- Do not include confidence scores.
- Do not include citations.
- Do not use markdown.
- Do not use bullet points unless they are absolutely necessary.

IMPORTANT:

The answer will later be checked against external evidence.
Therefore, separate the answer into clear, independent
factual claims.

Return ONLY valid JSON.

Use exactly this structure:

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

RULES FOR CLAIMS:

- Each claim should contain one main factual assertion.
- Avoid combining unrelated facts into one claim.
- Do not create unnecessary claims.
- Do not create claims about your own confidence.
- Do not include conversational filler.
- Do not include markdown.
- Return valid JSON only.
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
