import streamlit as st

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence

from ui import (
    load_css,
    display_header,
    display_first_question,
    display_quick_questions,
    display_question,
    display_claim,
    display_summary,
    display_analysis_header,
    display_how_it_works,
    display_question_prompt,
    display_clear_button
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="AI Confidence Layer",
    page_icon="🧠",
    layout="centered"
)


# ============================================================
# THEME
# ============================================================

load_css()

display_header()


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# PROCESS QUESTION
# ============================================================

def process_question(question):

    question = question.strip()

    with st.spinner("Thinking..."):

        result = generate_claims(question)


    analyzed_claims = []


    for claim in result.get("claims", []):

        claim_text = claim.get(
            "text",
            ""
        )


        if not claim_text:

            continue


        with st.spinner("Checking the evidence..."):

            evidence = find_evidence(
                claim_text
            )


        with st.spinner("Evaluating trustworthiness..."):

            confidence = calculate_confidence(
                claim_text,
                evidence
            )


        analyzed_claims.append(
            {
                "claim": claim_text,

                "confidence": confidence,

                "evidence": evidence
            }
        )


    st.session_state.messages.append(
        {
            "question": question,

            "analyzed_claims": analyzed_claims
        }
    )


# ============================================================
# FIRST SCREEN
# ============================================================

if len(st.session_state.messages) == 0:

    display_first_question()

    display_quick_questions()

    st.markdown("---")


# ============================================================
# QUESTION INPUT
# ============================================================

with st.form(
    "question_form",
    clear_on_submit=True
):

    question = st.text_input(
        "Question",

        placeholder=(
            "Ask anything — e.g. "
            "Is artificial intelligence conscious?"
        ),

        label_visibility="collapsed"
    )


    submitted = st.form_submit_button(
        "🔍  Analyze Answer"
    )


# ============================================================
# SUBMIT
# ============================================================

if submitted:

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        process_question(question)

        st.rerun()


# ============================================================
# CONVERSATION
# ============================================================

for message in st.session_state.messages:

    display_question(
        message["question"]
    )


    display_summary(
        message["analyzed_claims"]
    )


    display_analysis_header()


    for item in message["analyzed_claims"]:

        display_claim(
            item["claim"],
            item["confidence"],
            item["evidence"]
        )


    display_how_it_works()


# ============================================================
# FOLLOW-UP
# ============================================================

if len(st.session_state.messages) > 0:

    display_question_prompt()


    with st.form(
        "follow_up_question_form",
        clear_on_submit=True
    ):

        follow_up_question = st.text_input(
            "Follow-up question",

            placeholder=(
                "Ask a follow-up or explore something new..."
            ),

            label_visibility="collapsed"
        )


        follow_up_submitted = (
            st.form_submit_button(
                "↗  Ask another question"
            )
        )


    if follow_up_submitted:

        if not follow_up_question.strip():

            st.warning(
                "Please enter a question first."
            )

        else:

            process_question(
                follow_up_question
            )

            st.rerun()


    st.markdown("---")

    display_clear_button()
