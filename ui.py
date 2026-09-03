import streamlit as st


# ============================================================
# GLOBAL DESIGN
# ============================================================

def load_css():
    st.html("""
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
    );

    /* =========================
       MAIN PAGE
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 0% 0%,
                #dff7f0 0%,
                transparent 30%
            ),
            radial-gradient(
                circle at 100% 0%,
                #e3efff 0%,
                transparent 32%
            ),
            #f5f8fb;
        color: #172033 !important;
    }

    .main .block-container {
        max-width: 900px;
        padding-top: 2.5rem;
        padding-bottom: 5rem;
    }


    /* =========================
       TYPOGRAPHY
       ========================= */

    h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #10213f !important;
        font-weight: 700 !important;
    }

    h2 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #10213f !important;
        font-weight: 700 !important;
    }

    h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #183153 !important;
        font-weight: 700 !important;
    }

    p {
        font-family: 'DM Sans', sans-serif !important;
        color: #334155 !important;
    }

    span {
        font-family: 'DM Sans', sans-serif;
    }

    .stCaption,
    [data-testid="stCaptionContainer"] {
        color: #64748b !important;
    }


    /* =========================
       INPUT
       ========================= */

    div[data-baseweb="input"] {
        background: #ffffff !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 16px !important;
        box-shadow:
            0 4px 16px rgba(15, 23, 42, 0.07) !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #0f9d8a !important;
        box-shadow:
            0 0 0 4px rgba(15, 157, 138, 0.12),
            0 6px 20px rgba(15, 23, 42, 0.08) !important;
    }

    input {
        background: #ffffff !important;
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 1rem !important;
    }

    input::placeholder {
        color: #64748b !important;
        opacity: 1 !important;
    }


    /* =========================
       BUTTONS
       ========================= */

    .stButton > button,
    .stFormSubmitButton > button {
        background: #0f766e !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 14px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
        min-height: 46px !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: #0b5f59 !important;
        transform: translateY(-1px) !important;
        box-shadow:
            0 8px 20px rgba(15, 118, 110, 0.22) !important;
    }


    /* =========================
       METRICS
       ========================= */

    [data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #dbe4ec !important;
        border-radius: 15px !important;
        padding: 14px !important;
        box-shadow:
            0 4px 14px rgba(15, 23, 42, 0.05) !important;
    }

    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    [data-testid="stMetricValue"] {
        color: #10213f !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }


    /* =========================
       EXPANDERS
       ========================= */

    div[data-testid="stExpander"] {
        background: #ffffff !important;
        border: 1px solid #d8e2eb !important;
        border-radius: 15px !important;
        box-shadow:
            0 3px 12px rgba(15, 23, 42, 0.04) !important;
    }

    div[data-testid="stExpander"] summary {
        color: #183153 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
    }


    /* =========================
       ALERTS
       ========================= */

    div[data-testid="stAlert"] {
        border-radius: 15px !important;
    }


    /* =========================
       DIVIDERS
       ========================= */

    hr {
        border-color: #dbe4ec !important;
    }


    /* =========================
       SPINNER
       ========================= */

    [data-testid="stSpinner"] {
        color: #0f766e !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    </style>
    """)

# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown(
        """
        <div style="text-align:center;">
        """,
        unsafe_allow_html=False
    )

    st.markdown("### ✦ AI TRUST & EVIDENCE")

    st.title("AI Confidence Layer")

    st.markdown(
        "**Don't just get an AI answer.**  \n"
        "Understand **why** you should trust it."
    )

    st.markdown(
        "Your AI answer is broken into claims, checked against evidence, "
        "and given a transparent confidence level."
    )

    st.markdown("---")


# ============================================================
# FIRST QUESTION
# ============================================================

def display_first_question():

    st.markdown("## 👋 What are you curious about?")

    st.markdown(
        "Ask naturally. I'll break the answer into claims, "
        "check the evidence, and help you understand what deserves your trust."
    )

    st.markdown("")


# ============================================================
# QUESTION PROMPT
# ============================================================

def display_question_prompt():

    st.markdown("---")

    st.markdown("## 💬 Keep exploring")

    st.markdown(
        "Ask something related to your previous question, "
        "challenge a claim, or explore a completely different topic."
    )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown("## 🔎 Claim-by-Claim Analysis")

    st.caption(
        "Each part of the answer is evaluated separately against retrieved evidence."
    )


# ============================================================
# SUMMARY
# ============================================================

def display_summary(analyzed_claims):

    high = 0
    medium = 0
    low = 0
    speculative = 0

    for item in analyzed_claims:

        confidence = item.get("confidence", {})
        level = confidence.get("confidence", "LOW")

        if level == "HIGH":
            high += 1

        elif level == "MEDIUM":
            medium += 1

        elif level == "SPECULATIVE":
            speculative += 1

        else:
            low += 1

    st.markdown("### 🧭 Trust overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🟢 Strong", high)

    with col2:
        st.metric("🟡 Needs context", medium)

    with col3:
        st.metric("🟠 Speculative", speculative)

    with col4:
        st.metric("🔴 Low", low)


# ============================================================
# CLAIM
# ============================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get("confidence", "LOW")
    reason = confidence.get(
        "reason",
        "There is not enough information to determine reliability."
    )

    # --------------------------------------------------------
    # HIGH
    # --------------------------------------------------------

    if level == "HIGH":

        st.success(
            f"🟢 HIGH CONFIDENCE\n\n"
            f"**{claim}**"
        )

    # --------------------------------------------------------
    # MEDIUM
    # --------------------------------------------------------

    elif level == "MEDIUM":

        st.warning(
            f"🟡 MEDIUM CONFIDENCE\n\n"
            f"**{claim}**"
        )

    # --------------------------------------------------------
    # SPECULATIVE
    # --------------------------------------------------------

    elif level == "SPECULATIVE":

        st.info(
            f"🟠 SPECULATIVE / PURE GENERATION\n\n"
            f"**{claim}**"
        )

    # --------------------------------------------------------
    # LOW
    # --------------------------------------------------------

    else:

        st.error(
            f"🔴 LOW CONFIDENCE\n\n"
            f"**{claim}**"
        )

    # --------------------------------------------------------
    # WHY
    # --------------------------------------------------------

    st.markdown("**Why this rating?**")

    st.write(reason)

    # --------------------------------------------------------
    # EVIDENCE
    # --------------------------------------------------------

    if evidence:

        with st.expander(
            f"📚 View supporting evidence ({len(evidence)} sources)"
        ):

            for index, source in enumerate(evidence, start=1):

                title = source.get(
                    "title",
                    f"Source {index}"
                )

                content = source.get(
                    "content",
                    "No preview available."
                )

                url = source.get(
                    "url",
                    ""
                )

                st.markdown(f"**{index}. {title}**")

                st.write(content)

                if url:
                    st.markdown(
                        f"[↗ Open source]({url})"
                    )

                if index < len(evidence):
                    st.markdown("---")

    else:

        st.warning(
            "🟠 No external evidence was retrieved for this claim. "
            "Treat it as unverified rather than automatically true."
        )

    st.markdown("")


# ============================================================
# CONVERSATIONAL AI ANSWER
# ============================================================

def display_ai_answer(answer):

    if not answer:
        return

    st.markdown("### 🤖 Here's what I found")

    st.info(answer)


# ============================================================
# USER QUESTION
# ============================================================

def display_user_question(question):

    st.markdown("### 👤 Your question")

    st.markdown(f"> {question}")

    st.markdown("")
