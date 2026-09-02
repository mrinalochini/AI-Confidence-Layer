import streamlit as st

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence

from ui import (
    load_css,
    display_header,
    display_claim,
    display_summary
)

load_css()
display_header()

question = st.text_input(
    "Ask a question",
    placeholder="Example: Who invented the telephone?"
)

if st.button("🔍 Analyze Answer"):

    if not question:
        st.warning("Please enter a question.")

    else:

        with st.spinner("🧠 Generating and separating claims..."):

            result = generate_claims(question)

        analyzed_claims = []

        for claim in result["claims"]:

            claim_id = claim["id"]
            claim_text = claim["text"]

            with st.spinner(
                f"🔎 Finding evidence for Claim {claim_id}..."
            ):

                evidence = find_evidence(claim_text)

            with st.spinner(
                f"🧠 Evaluating Claim {claim_id}..."
            ):

                confidence = calculate_confidence(
                    claim_text,
                    evidence
                )

            analyzed_claims.append({
                "claim": claim_text,
                "confidence": confidence,
                "evidence": evidence
            })

        display_summary(analyzed_claims)

        st.markdown(
            '<div class="section-title">🔬 Claim-by-Claim Analysis</div>',
            unsafe_allow_html=True
        )

        for item in analyzed_claims:

            display_claim(
                item["claim"],
                item["confidence"],
                item["evidence"]
            )
