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


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


if "has_answer" not in st.session_state:
    st.session_state.has_answer = False


# =========================================================
# HERO
# =========================================================

display_header()


# =========================================================
# QUESTION INPUT
# =========================================================

if not st.session_state.has_answer:

    # -----------------------------------------------------
    # FIRST QUESTION
    # -----------------------------------------------------

    st.markdown(
        """
        <div style="
            margin-top:20px;
            margin-bottom:10px;
            font-family:'Space Grotesk', sans-serif;
            font-size:18px;
            font-weight:700;
            color:#27324A;
        ">
            What would you like to know?
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            margin-bottom:13px;
            font-family:'DM Sans', sans-serif;
            font-size:14px;
            color:#7B8499;
        ">
            Ask a question and we'll help you understand
            how much you can trust the answer.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FORM
# =========================================================

with st.form("question_form", clear_on_submit=True):

    question = st.text_input(
        "Question",
        placeholder=(
            "Example: Who invented the telephone?"
        ),
        label_visibility="collapsed"
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
            "Please enter a question first."
        )

    else:

        question = question.strip()

        # -------------------------------------------------
        # SAVE QUESTION
        # -------------------------------------------------

        st.session_state.messages.append({
            "question": question
        })


        # -------------------------------------------------
        # GENERATE CLAIMS
        # -------------------------------------------------

        with st.spinner("Thinking..."):

            result = generate_claims(question)


        analyzed_claims = []


        # -------------------------------------------------
        # PROCESS EACH CLAIM
        # -------------------------------------------------

        for claim in result["claims"]:

            claim_text = claim["text"]


            # ---------------------------------------------
            # RETRIEVE EVIDENCE
            # ---------------------------------------------

            with st.spinner("Processing..."):

                evidence = find_evidence(
                    claim_text
                )


            # ---------------------------------------------
            # CALCULATE CONFIDENCE
            # ---------------------------------------------

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


        # -------------------------------------------------
        # SAVE RESULT
        # -------------------------------------------------

        st.session_state.messages[-1][
            "analyzed_claims"
        ] = analyzed_claims


        st.session_state.has_answer = True


        # -------------------------------------------------
        # FORCE RERUN
        # -------------------------------------------------

        st.rerun()


# =========================================================
# DISPLAY PREVIOUS QUESTIONS / ANSWERS
# =========================================================

for message in st.session_state.messages:

    if "analyzed_claims" not in message:
        continue


    # -----------------------------------------------------
    # QUESTION DISPLAY
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div style="
            margin-top:32px;
            margin-bottom:18px;
            padding:18px 20px;

            background:
                linear-gradient(
                    135deg,
                    #F5F1FF,
                    #EFFAFF
                );

            border:1px solid #DFE2F1;

            border-radius:18px;
        ">

            <div style="
                font-family:'Space Grotesk', sans-serif;
                font-size:10px;
                font-weight:700;
                color:#8067D9;
                letter-spacing:1.2px;
                text-transform:uppercase;
                margin-bottom:7px;
            ">
                YOUR QUESTION
            </div>

            <div style="
                font-family:'Manrope', sans-serif;
                font-size:18px;
                font-weight:700;
                line-height:1.5;
                color:#273149;
            ">
                {question if False else message["question"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    display_summary(
        message["analyzed_claims"]
    )


    # -----------------------------------------------------
    # CLAIM ANALYSIS
    # -----------------------------------------------------

    display_analysis_header()


    for item in message["analyzed_claims"]:

        display_claim(
            item["claim"],
            item["confidence"],
            item["evidence"]
        )


# =========================================================
# FOLLOW-UP COMPOSER
# =========================================================

if st.session_state.has_answer:

    display_question_prompt()


    # -----------------------------------------------------
    # SECOND / FOLLOW-UP QUESTION
    # -----------------------------------------------------

    with st.form(
        "follow_up_question_form",
        clear_on_submit=True
    ):

        follow_up_question = st.text_input(
            "Follow-up question",
            placeholder=(
                "Ask a related question or explore something new..."
            ),
            label_visibility="collapsed"
        )


        follow_up_submitted = st.form_submit_button(
            "🔍  Analyze Answer",
            use_container_width=False
        )


    # -----------------------------------------------------
    # PROCESS FOLLOW-UP
    # -----------------------------------------------------

    if follow_up_submitted:

        if not follow_up_question.strip():

            st.warning(
                "Please enter a question first."
            )

        else:

            follow_up_question = (
                follow_up_question.strip()
            )


            # ---------------------------------------------
            # SAVE NEW QUESTION
            # ---------------------------------------------

            st.session_state.messages.append({
                "question": follow_up_question
            })


            # ---------------------------------------------
            # GENERATE
            # ---------------------------------------------

            with st.spinner("Thinking..."):

                result = generate_claims(
                    follow_up_question
                )


            analyzed_claims = []


            # ---------------------------------------------
            # CLAIMS
            # ---------------------------------------------

            for claim in result["claims"]:

                claim_text = claim["text"]


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


            # ---------------------------------------------
            # SAVE
            # ---------------------------------------------

            st.session_state.messages[-1][
                "analyzed_claims"
            ] = analyzed_claims


            # ---------------------------------------------
            # RERUN
            # ---------------------------------------------

            st.rerun()
