import streamlit as st

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence

from ui import (
    display_header,
    display_first_question,
    display_claim,
    display_summary,
    display_analysis_header,
    display_question_prompt
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Confidence Layer",
    page_icon="🧠",
    layout="centered"
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# HEADER
# ============================================================

display_header()


# ============================================================
# QUESTION PROCESSING FUNCTION
# ============================================================

def process_question(question):

    question = question.strip()


    # --------------------------------------------------------
    # GENERATE AI CLAIMS
    # --------------------------------------------------------

    with st.spinner("Thinking..."):

        result = generate_claims(question)


    analyzed_claims = []


    # --------------------------------------------------------
    # ANALYZE EACH CLAIM
    # --------------------------------------------------------

    for claim in result.get("claims", []):

        claim_text = claim.get(
            "text",
            ""
        )


        if not claim_text:

            continue


        # ----------------------------------------------------
        # FIND EVIDENCE
        # ----------------------------------------------------

        with st.spinner("Processing..."):

            evidence = find_evidence(
                claim_text
            )


        # ----------------------------------------------------
        # CALCULATE CONFIDENCE
        # ----------------------------------------------------

        with st.spinner("Evaluating..."):

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


    # --------------------------------------------------------
    # SAVE CONVERSATION
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "question": question,
            "analyzed_claims": analyzed_claims
        }
    )


# ============================================================
# FIRST QUESTION
# ============================================================

if len(st.session_state.messages) == 0:

    display_first_question()


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
            "Example: Who invented the telephone?"
        ),
        label_visibility="collapsed"
    )


    submitted = st.form_submit_button(
        "🔍  Analyze Answer"
    )


# ============================================================
# PROCESS QUESTION
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
# DISPLAY ALL ANSWERS
# ============================================================

for message in st.session_state.messages:


    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.markdown(
        "### 👤 Your Question"
    )

    st.write(
        message["question"]
    )


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    display_summary(
        message["analyzed_claims"]
    )


    # --------------------------------------------------------
    # CLAIM ANALYSIS
    # --------------------------------------------------------

    display_analysis_header()


    for item in message["analyzed_claims"]:

        display_claim(
            item["claim"],
            item["confidence"],
            item["evidence"]
        )


# ============================================================
# FOLLOW-UP QUESTION
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
                "Ask something related or "
                "explore a new topic..."
            ),
            label_visibility="collapsed"
        )


        follow_up_submitted = st.form_submit_button(
            "🔍  Analyze Answer"
        )


    # --------------------------------------------------------
    # PROCESS FOLLOW-UP
    # --------------------------------------------------------

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
