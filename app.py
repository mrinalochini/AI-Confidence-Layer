import streamlit as st

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence

from ui import (
    load_css,
    display_header,
    display_claim,
    display_summary,
    display_analysis_header
)


# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="AI Confidence Layer",
    page_icon="🧠",
    layout="centered"
)

load_css()

display_header()


# =========================================================
# QUESTION AREA
# =========================================================

st.markdown(
    """
    <div style="
        margin-top: 10px;
        margin-bottom: 8px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 19px;
        font-weight: 700;
        color: #343b53;
    ">
        💬 What would you like to know?
    </div>

    <div style="
        margin-bottom: 14px;
        font-family: 'Quicksand', sans-serif;
        font-size: 14px;
        color: #7a8397;
    ">
        Ask anything and we'll help you understand how much you can trust the answer.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FORM
# =========================================================

with st.form(
    key="question_form",
    clear_on_submit=False
):

    question = st.text_input(
        "Question",
        placeholder="Try: Who invented the telephone?",
        label_visibility="collapsed",
        key="question_input"
    )

    submitted = st.form_submit_button(
        "🔍  Analyze Answer",
        use_container_width=False
    )


# =========================================================
# PROCESS QUESTION
# =========================================================

if submitted:

    if not question.strip():

        st.warning(
            "✨ Please enter a question first."
        )

    else:

        # -------------------------------------------------
        # ONE SIMPLE PROCESSING MESSAGE
        # -------------------------------------------------

        with st.spinner(
            "🧠 Thinking... This may take a few minutes."
        ):

            # Generate claims
            result = generate_claims(question)

            analyzed_claims = []


            # -------------------------------------------------
            # PROCESS EVERYTHING QUIETLY
            # -------------------------------------------------

            for claim in result["claims"]:

                claim_text = claim["text"]


                # Find supporting evidence
                evidence = find_evidence(
                    claim_text
                )


                # Calculate confidence
                confidence = calculate_confidence(
                    claim_text,
                    evidence
                )


                analyzed_claims.append({

                    "claim": claim_text,

                    "confidence": confidence,

                    "evidence": evidence

                })


        # =================================================
        # RESULTS
        # =================================================

        if analyzed_claims:

            display_summary(
                analyzed_claims
            )

            display_analysis_header()


            for item in analyzed_claims:

                display_claim(
                    item["claim"],
                    item["confidence"],
                    item["evidence"]
                )


            # =================================================
            # ASK ANOTHER QUESTION
            # =================================================

            st.markdown(
                """
                <div style="
                    text-align:center;
                    margin-top:45px;
                    margin-bottom:10px;
                    font-family:'Playfair Display', serif;
                    font-size:25px;
                    font-weight:700;
                    color:#343b53;
                ">
                    💭 Have another question?
                </div>

                <div style="
                    text-align:center;
                    margin-bottom:25px;
                    font-family:'Quicksand', sans-serif;
                    font-size:15px;
                    color:#7a8397;
                ">
                    Ask another question above and discover whether
                    you can trust that answer too.
                </div>
                """,
                unsafe_allow_html=True
            )
