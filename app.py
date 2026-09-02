import streamlit as st

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence

from ui import (
    load_css,
    display_header,
    display_claim,
    display_summary,
    display_analysis_header,
    display_question_prompt
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Confidence Layer",
    page_icon="🧠",
    layout="centered"
)


# =========================================================
# LOAD UI
# =========================================================

load_css()

display_header()


# =========================================================
# ANALYSIS FUNCTION
# =========================================================

def analyze_question(question):

    with st.spinner(
        "🧠 Thinking... This may take a few minutes."
    ):

        # ---------------------------------------------
        # GENERATE CLAIMS
        # ---------------------------------------------

        result = generate_claims(
            question
        )


        analyzed_claims = []


        # ---------------------------------------------
        # PROCESS CLAIMS
        # ---------------------------------------------

        for claim in result["claims"]:

            claim_text = claim["text"]


            # Find evidence
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


    return analyzed_claims


# =========================================================
# FIRST QUESTION
# =========================================================

with st.form(
    "main_question_form",
    clear_on_submit=False
):

    st.markdown(
        """
        <div style="
            font-family:'Space Grotesk',sans-serif;
            font-size:19px;
            font-weight:700;
            color:#343B53;
            margin-bottom:7px;
        ">
            💬 What would you like to know?
        </div>

        <div style="
            font-family:'Quicksand',sans-serif;
            font-size:14px;
            color:#7A8195;
            margin-bottom:13px;
        ">
            Ask anything and we'll help you understand how much
            you can trust the answer.
        </div>
        """,
        unsafe_allow_html=True
    )


    question = st.text_input(
        "Question",
        placeholder="Try: Who invented the telephone?",
        label_visibility="collapsed",
        key="main_question"
    )


    submitted = st.form_submit_button(
        "🔍  Analyze Answer"
    )


# =========================================================
# PROCESS FIRST QUESTION
# =========================================================

if submitted:

    if not question.strip():

        st.warning(
            "✨ Please enter a question first."
        )

    else:

        st.session_state["question"] = question

        st.session_state["analyzed_claims"] = (
            analyze_question(question)
        )


# =========================================================
# DISPLAY CURRENT ANSWER
# =========================================================

if "analyzed_claims" in st.session_state:

    analyzed_claims = (
        st.session_state["analyzed_claims"]
    )


    if analyzed_claims:

        # ---------------------------------------------
        # TRUST SUMMARY
        # ---------------------------------------------

        display_summary(
            analyzed_claims
        )


        # ---------------------------------------------
        # CLAIM ANALYSIS
        # ---------------------------------------------

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

        display_question_prompt()


        with st.form(
            "another_question_form",
            clear_on_submit=False
        ):

            another_question = st.text_input(
                "Another question",
                placeholder="Ask another question...",
                label_visibility="collapsed",
                key="another_question"
            )


            another_submitted = st.form_submit_button(
                "✨  Analyze New Question"
            )


        # =================================================
        # PROCESS NEW QUESTION
        # =================================================

        if another_submitted:

            if not another_question.strip():

                st.warning(
                    "✨ Please enter a question first."
                )

            else:

                st.session_state["question"] = (
                    another_question
                )

                st.session_state["analyzed_claims"] = (
                    analyze_question(
                        another_question
                    )
                )

                st.rerun()
