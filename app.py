import streamlit as st
import os

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence
from ui import (
    load_css,
    display_header,
    display_claim,
    display_summary
)


# -------------------------------
# FRONTEND
# -------------------------------

load_css()
display_header()


# -------------------------------
# QUESTION INPUT
# -------------------------------

st.title("AI Confidence Layer")

question = st.text_input(
    "Ask a question:"
)


if st.button("Analyze"):

    if not question:

        st.warning("Please enter a question.")

    else:

        # MEMBER 1
        with st.spinner("Generating claims..."):

            result = generate_claims(question)


        st.subheader("Confidence Analysis")


        # Process every claim
        for claim in result["claims"]:

            claim_id = claim["id"]
            claim_text = claim["text"]


            # MEMBER 2
            with st.spinner(
                f"Finding evidence for Claim {claim_id}..."
            ):

                evidence = find_evidence(
                    claim_text
                )


            # MEMBER 3
            with st.spinner(
                f"Checking Claim {claim_id}..."
            ):

                confidence = calculate_confidence(
                    claim_text,
                    evidence
                )


            # MEMBER 4
            display_claim(
                claim_text,
                confidence,
                evidence
            )
