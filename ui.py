import streamlit as st


# ============================================================
# GLOBAL DESIGN
# ============================================================

def load_css():
    st.html("""
    <style>

    /* ---------- GOOGLE FONTS ---------- */

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
    );

    /* ---------- PAGE ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(82, 183, 136, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(72, 149, 239, 0.12),
                transparent 30%
            ),
            #f8fafc;
    }

    .main .block-container {
        max-width: 900px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* ---------- DEFAULT TEXT ---------- */

    html,
    body,
    [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    p,
    label,
    span {
        font-family: 'DM Sans', sans-serif;
    }

    h1,
    h2,
    h3 {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    /* ---------- INPUT ---------- */

    div[data-baseweb="input"] {
        border-radius: 16px !important;
        border: 1px solid #d6dee8 !important;
        background: #ffffff !important;
        box-shadow: 0 4px 18px rgba(15, 23, 42, 0.06);
    }

    div[data-baseweb="input"]:focus-within {
        border: 1px solid #4895ef !important;
        box-shadow:
            0 0 0 3px rgba(72, 149, 239, 0.14),
            0 6px 22px rgba(15, 23, 42, 0.07);
    }

    input {
        color: #172033 !important;
        background: transparent !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 1rem !important;
    }

    input::placeholder {
        color: #8290a3 !important;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 14px !important;
        border: none !important;
        background: #2563eb !important;
        color: white !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
        min-height: 44px !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: #1d4ed8 !important;
        transform: translateY(-1px);
        box-shadow: 0 7px 18px rgba(37, 99, 235, 0.22);
    }

    /* ---------- EXPANDERS ---------- */

    div[data-testid="stExpander"] {
        border: 1px solid #dce4ed !important;
        border-radius: 15px !important;
        background: #ffffff !important;
        overflow: hidden;
    }

    div[data-testid="stExpander"] summary {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
        color: #263449 !important;
    }

    /* ---------- ALERTS ---------- */

    div[data-testid="stAlert"] {
        border-radius: 14px;
    }

    /* ---------- DIVIDERS ---------- */

    hr {
        border-color: #e2e8f0 !important;
    }

    /* ---------- SPINNER ---------- */

    div[data-testid="stSpinner"] {
        font-family: 'DM Sans', sans-serif;
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
