import json
import os
from openai import OpenAI


def calculate_confidence(claim, evidence):

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    evidence_text = "\n\n".join(
        item["content"] for item in evidence
    )

    prompt = f"""
You are a claim verification system.

Determine whether the evidence supports the claim.

CLAIM:
{claim}

EVIDENCE:
{evidence_text}

Classify the claim as one of:

HIGH
MEDIUM
LOW

HIGH:
The evidence directly supports the claim.

MEDIUM:
The evidence partially supports the claim or
requires a reasonable inference.

LOW:
The evidence does not support the claim,
contradicts it, or there is insufficient evidence.

Return ONLY valid JSON:

if len(evidence) == 0:
    return {
        "confidence": "SPECULATIVE",
        "reason": "No retrieved evidence supports this claim. The model generated this statement based on its internal knowledge or creative inference."
    }
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"},
        stream=False
    )

    return json.loads(
        response.choices[0].message.content
    )
