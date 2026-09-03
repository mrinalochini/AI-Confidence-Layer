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


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Confidence Layer",
    page_icon="🧠",
    layout="centered"
)


# ============================================================
# LOAD UI
# ============================================================

load_css()


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "has_answer" not in st.session_state:
    st.session_state.has_answer = False


# ============================================================
# HERO
# ============================================================

display_header()


# ============================================================
# FIRST QUESTION
# ============================================================

if not st.session_state.has_answer:

    st.markdown(
        "<div class='question-heading'>What would you like to know?</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='question-subheading'>"
        "Ask a question and we'll help you understand "
        "how much you can trust the answer."
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# QUESTION FORM
# ============================================================

with st.form("question_form", clear_on_submit=True):

    question = st.text_input(
        "Question",
        placeholder="Ask anything...",
        label_visibility="collapsed"
    )

    submitted = st.form_submit_button(
        "🔍  Analyze Answer"
    )


# ============================================================
# PROCESS FIRST / NEW QUESTION
# ============================================================

if submitted:

    if not question.strip():

        st.warning("Please enter a question first.")

    else:

        question = question.strip()

        # Save question
        st.session_state.messages.append({
            "question": question
        })

        # -----------------------------------------------
        # THINKING
        # -----------------------------------------------

        with st.spinner("Thinking..."):

            result = generate_claims(question)

        analyzed_claims = []

        # -----------------------------------------------
        # PROCESS CLAIMS
        # -----------------------------------------------

        for claim in result.get("claims", []):

            claim_text = claim.get("text", "")

            # Evidence
            with st.spinner("Processing..."):

                evidence = find_evidence(claim_text)

            # Confidence
            with st.spinner("Evaluating..."):

                confidence = calculate_confidence(
                    claim_text,
                    evidence
                )

            analyzed_claims.append({
                "claim": claim_text,
                "confidence": confidence,
                "evidence": evidence
            })

        # -----------------------------------------------
        # SAVE RESULT
        # -----------------------------------------------

        st.session_state.messages[-1][
            "analyzed_claims"
        ] = analyzed_claims

        st.session_state.has_answer = True

        # Refresh page
        st.rerun()


# ============================================================
# DISPLAY ALL PREVIOUS QUESTIONS / ANSWERS
# ============================================================

for message in st.session_state.messages:

    if "analyzed_claims" not in message:
        continue

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.markdown(
        "<div class='user-question-card'>"
        "<div class='user-question-label'>YOUR QUESTION</div>"
        f"<div class='user-question-text'>"
        f"{message['question']}"
        "</div>"
        "</div>",
        unsafe_allow_html=True
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

if st.session_state.has_answer:

    display_question_prompt()

    with st.form(
        "follow_up_question_form",
        clear_on_submit=True
    ):

        follow_up_question = st.text_input(
            "Follow-up question",
            placeholder=(
                "Ask something related or explore a new topic..."
            ),
            label_visibility="collapsed"
        )

        follow_up_submitted = st.form_submit_button(
            "🔍  Analyze Answer"
        )


    # ========================================================
    # PROCESS FOLLOW-UP
    # ========================================================

    if follow_up_submitted:

        if not follow_up_question.strip():

            st.warning("Please enter a question first.")

        else:

            follow_up_question = (
                follow_up_question.strip()
            )

            # -----------------------------------------------
            # SAVE QUESTION
            # -----------------------------------------------

            st.session_state.messages.append({
                "question": follow_up_question
            })

            # -----------------------------------------------
            # THINKING
            # -----------------------------------------------

            with st.spinner("Thinking..."):

                result = generate_claims(
                    follow_up_question
                )

            analyzed_claims = []

            # -----------------------------------------------
            # PROCESS
            # -----------------------------------------------

            for claim in result.get("claims", []):

                claim_text = claim.get("text", "")

                with st.spinner("Processing..."):

                    evidence = find_evidence(
                        claim_text
                    )

                with st.spinner("Evaluating..."):

                    confidence = calculate_confidence(
                        claim_text,
                        evidence
                    )

                analyzed_claims.append({
                    "claim": claim_text,
                    "confidence": confidence,
                    "evidence": evidence
                })

            # -----------------------------------------------
            # SAVE
            # -----------------------------------------------

            st.session_state.messages[-1][
                "analyzed_claims"
            ] = analyzed_claims

            st.rerun()
