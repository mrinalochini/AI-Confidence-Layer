import streamlit as st

from llm_engine import generate_claims
from evidence_engine import find_evidence
from confidence_engine import calculate_confidence

from ui import (
    load_css,
    display_header,
    display_first_question,
    display_user_question,
    display_ai_answer,
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
# DESIGN
# ============================================================

load_css()


# ============================================================
# HEADER
# ============================================================

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

    # --------------------------------------------------------
    # AI ANSWER
    # --------------------------------------------------------

    with st.spinner("Thinking..."):

        result = generate_claims(question)

    # --------------------------------------------------------
    # CLAIMS
    # --------------------------------------------------------

    analyzed_claims = []

    for claim in result.get("claims", []):

        claim_text = claim.get("text", "").strip()

        if not claim_text:
            continue

        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        with st.spinner("Checking the evidence..."):

            evidence = find_evidence(claim_text)

        # ----------------------------------------------------
        # CONFIDENCE
        # ----------------------------------------------------

        with st.spinner("Evaluating trust..."):

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
            "answer": result.get("answer", ""),
            "analyzed_claims": analyzed_claims
        }
    )


# ============================================================
# FIRST SCREEN
# ============================================================

if len(st.session_state.messages) == 0:

    display_first_question()


# ============================================================
# QUESTION FORM
# ============================================================

with st.form(
    "question_form",
    clear_on_submit=True
):

    question = st.text_input(
        "Question",
        placeholder="Try: Is artificial intelligence replacing jobs?",
        label_visibility="collapsed"
    )

    submitted = st.form_submit_button(
        "🔍 Analyze Answer",
        use_container_width=True
    )


# ============================================================
# SUBMIT
# ============================================================

if submitted:

    if not question.strip():

        st.warning(
            "Tell me what's on your mind first 😊"
        )

    else:

        process_question(question)

        st.rerun()


# ============================================================
# DISPLAY CONVERSATION
# ============================================================

for message in st.session_state.messages:

    st.markdown("---")

    display_user_question(
        message["question"]
    )

    # --------------------------------------------------------
    # NATURAL AI ANSWER
    # --------------------------------------------------------

    display_ai_answer(
        message.get("answer", "")
    )

    # --------------------------------------------------------
    # TRUST SUMMARY
    # --------------------------------------------------------

    display_summary(
        message["analyzed_claims"]
    )

    st.markdown("")

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
            placeholder="Ask a follow-up or explore something completely new...",
            label_visibility="collapsed"
        )

        follow_up_submitted = st.form_submit_button(
            "✨ Ask AI",
            use_container_width=True
        )

    if follow_up_submitted:

        if not follow_up_question.strip():

            st.warning(
                "What would you like to explore? 😊"
            )

        else:

            process_question(
                follow_up_question
            )

            st.rerun()
