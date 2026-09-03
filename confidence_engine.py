import json
import streamlit as st
from openai import OpenAI


def calculate_confidence(claim, evidence):

    if not evidence:
        return {
            "confidence": "SPECULATIVE",
            "reason": (
                "No external evidence was retrieved for this claim, "
                "so it should be treated as unverified."
            )
        }

    # existing LLM verification code below...


    # =====================================================
    # GROQ CLIENT
    # =====================================================

    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )


    # =====================================================
    # PREPARE EVIDENCE
    # =====================================================

    evidence_text = "\n\n".join(

        f"Source: {item.get('title', 'Unknown source')}\n"
        f"{item.get('content', '')}"

        for item in evidence

    )


    # =====================================================
    # VERIFICATION PROMPT
    # =====================================================

    prompt = f"""
You are an evidence verification system.

Your job is to determine how strongly the retrieved evidence
supports the claim.

CLAIM:
{claim}

RETRIEVED EVIDENCE:
{evidence_text}


Classify the claim using exactly ONE of these labels:

HIGH
MEDIUM
LOW


HIGH:
The retrieved evidence directly and clearly supports
the claim.

MEDIUM:
The evidence partially supports the claim, or the claim
requires a reasonable inference from the evidence.

LOW:
The evidence does not adequately support the claim,
contradicts the claim, or the evidence is insufficient.


Return ONLY valid JSON in this exact format:

{{
    "confidence": "HIGH",
    "reason": "Short explanation of why the evidence supports or does not support the claim."
}}

Do not include markdown.
Do not include additional fields.
"""


    # =====================================================
    # ASK MODEL
    # =====================================================

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


    # =====================================================
    # GET RESPONSE
    # =====================================================

    answer = response.choices[0].message.content.strip()


    # =====================================================
    # REMOVE MARKDOWN CODE FENCES IF MODEL ADDS THEM
    # =====================================================

    if answer.startswith("```"):

        answer = answer.replace(
            "```json",
            ""
        )

        answer = answer.replace(
            "```",
            ""
        )

        answer = answer.strip()


    # =====================================================
    # PARSE JSON
    # =====================================================

    try:

        result = json.loads(answer)

    except json.JSONDecodeError:

        # Safe fallback instead of crashing the entire app

        return {
            "confidence": "LOW",
            "reason": (
                "The verification system could not reliably "
                "interpret the evidence."
            )
        }


    # =====================================================
    # VALIDATE CONFIDENCE
    # =====================================================

    valid_levels = {
        "HIGH",
        "MEDIUM",
        "LOW"
    }

    confidence_level = str(
        result.get(
            "confidence",
            "LOW"
        )
    ).upper()


    if confidence_level not in valid_levels:

        confidence_level = "LOW"


    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {

        "confidence": confidence_level,

        "reason": str(
            result.get(
                "reason",
                "No explanation was provided."
            )
        )

    }
