import streamlit as st


# ============================================================
# GLOBAL THEME
# ============================================================

def load_css():

    st.html("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');


    /* ========================================================
       MAIN APP
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(124, 92, 255, 0.18),
                transparent 27%
            ),
            radial-gradient(
                circle at 95% 10%,
                rgba(0, 207, 255, 0.15),
                transparent 27%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(255, 92, 205, 0.10),
                transparent 32%
            ),
            linear-gradient(
                135deg,
                #F8F7FF 0%,
                #F4F7FF 50%,
                #EFFBFC 100%
            );

        color: #172033;
    }


    /* ========================================================
       CONTENT WIDTH
       ======================================================== */

    .block-container {
        max-width: 900px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }


    /* ========================================================
       FONTS
       ======================================================== */

    html,
    body,
    [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    h1,
    h2,
    h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #172033 !important;
        letter-spacing: -0.035em;
    }


    /* ========================================================
       HIDE STREAMLIT BRANDING
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ========================================================
       MAIN TITLE
       ======================================================== */

    [data-testid="stHeading"] h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 3.4rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.055em !important;

        background: linear-gradient(
            90deg,
            #7048F5,
            #8759F5,
            #536DFF,
            #00AFCB
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    /* ========================================================
       NORMAL TEXT
       ======================================================== */

    p {
        font-family: 'DM Sans', sans-serif !important;
        color: #66728A;
    }


    /* ========================================================
       QUESTION INPUT
       ======================================================== */

    .stTextInput > div > div > input {

        background: rgba(255, 255, 255, 0.95) !important;

        color: #18233D !important;

        border: 1.5px solid rgba(112, 72, 245, 0.18) !important;

        border-radius: 18px !important;

        padding: 0.85rem 1.1rem !important;

        font-family: 'DM Sans', sans-serif !important;

        font-size: 1rem !important;

        box-shadow:
            0 8px 30px rgba(64, 51, 130, 0.07);

        transition: all 0.2s ease;
    }

    .stTextInput > div > div > input:focus {

        border-color: #7655E8 !important;

        box-shadow:
            0 0 0 4px rgba(118, 85, 232, 0.10),
            0 12px 35px rgba(74, 57, 140, 0.10);

        outline: none !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #98A0B5 !important;
    }


    /* ========================================================
       ANALYZE BUTTON
       ======================================================== */

    .stFormSubmitButton > button,
    .stButton > button {

        width: 100%;

        min-height: 48px;

        border: none !important;

        border-radius: 15px !important;

        background: linear-gradient(
            135deg,
            #7048F5,
            #5B6CFF,
            #00B8D9
        ) !important;

        color: white !important;

        font-family: 'DM Sans', sans-serif !important;

        font-size: 0.98rem !important;

        font-weight: 700 !important;

        box-shadow:
            0 10px 25px rgba(99, 79, 230, 0.23);

        transition: all 0.18s ease;
    }

    .stFormSubmitButton > button:hover,
    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 15px 32px rgba(99, 79, 230, 0.30);
    }


    /* ========================================================
       METRICS
       ======================================================== */

    [data-testid="stMetric"] {

        background: rgba(255, 255, 255, 0.78);

        border: 1px solid rgba(118, 85, 232, 0.11);

        border-radius: 18px;

        padding: 1rem;

        box-shadow:
            0 8px 25px rgba(40, 50, 90, 0.05);
    }

    [data-testid="stMetricLabel"] {

        font-family: 'DM Sans', sans-serif !important;

        color: #737E95 !important;
    }

    [data-testid="stMetricValue"] {

        font-family: 'Space Grotesk', sans-serif !important;

        color: #252D49 !important;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    .stExpander {

        background: rgba(255, 255, 255, 0.72) !important;

        border: 1px solid rgba(118, 85, 232, 0.12) !important;

        border-radius: 16px !important;

        box-shadow:
            0 7px 22px rgba(45, 54, 90, 0.04);
    }

    .stExpander summary {

        font-family: 'DM Sans', sans-serif !important;

        font-weight: 700 !important;

        color: #3C4562 !important;
    }


    /* ========================================================
       LINK BUTTONS
       ======================================================== */

    .stLinkButton > a {

        border-radius: 10px !important;

        border: 1px solid rgba(118, 85, 232, 0.20) !important;

        color: #6849D9 !important;

        background: #F7F4FF !important;

        font-family: 'DM Sans', sans-serif !important;

        font-weight: 700 !important;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    .stAlert {

        border-radius: 15px !important;

        font-family: 'DM Sans', sans-serif !important;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {

        border: none !important;

        height: 1px !important;

        background: linear-gradient(
            90deg,
            transparent,
            rgba(118, 85, 232, 0.20),
            rgba(0, 184, 217, 0.20),
            transparent
        ) !important;

        margin: 2rem 0 !important;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 700px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        [data-testid="stHeading"] h1 {
            font-size: 2.4rem !important;
        }
    }

    </style>
    """)


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.title("🧠 AI Confidence Layer")

    st.markdown(
        "Don't just get an AI answer."
    )

    st.markdown(
        "**Understand why you should trust it.**"
    )

    st.markdown("---")


# ============================================================
# FIRST QUESTION
# ============================================================

def display_first_question():

    st.markdown(
        "### What would you like to know?"
    )

    st.caption(
        "Ask anything and we'll show you how trustworthy the answer is."
    )


# ============================================================
# QUESTION DISPLAY
# ============================================================

def display_question(question):

    st.markdown("### 👤 Your Question")

    with st.container(border=True):

        st.markdown(
            f"**{question}**"
        )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown("### ✦ Claim-by-Claim Analysis")

    st.caption(
        "Each statement is evaluated against retrieved evidence."
    )


# ============================================================
# CLAIM
# ============================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get(
        "confidence",
        "LOW"
    ).upper()

    reason = confidence.get(
        "reason",
        "There is not enough evidence to determine reliability."
    )


    # --------------------------------------------------------
    # Claim container
    # --------------------------------------------------------

    with st.container(border=True):

        st.caption("AI CLAIM")

        st.markdown(
            f"**{claim}**"
        )


        # ----------------------------------------------------
        # Confidence state
        # ----------------------------------------------------

        if level == "HIGH":

            st.success(
                "🟢 HIGH CONFIDENCE"
            )

        elif level == "MEDIUM":

            st.warning(
                "🟡 MEDIUM CONFIDENCE"
            )

        elif level in [
            "SPECULATIVE",
            "PURE GENERATION"
        ]:

            st.warning(
                "🟠 SPECULATIVE — Pure Generation"
            )

        else:

            st.error(
                "🔴 LOW CONFIDENCE"
            )


        # ----------------------------------------------------
        # Reason
        # ----------------------------------------------------

        st.markdown("**Why this rating?**")

        st.info(reason)


        # ----------------------------------------------------
        # Evidence
        # ----------------------------------------------------

        st.markdown("**Supporting Evidence**")

        if not evidence:

            st.warning(
                "No supporting sources were found. "
                "Treat this statement as speculative."
            )

        else:

            with st.expander(
                f"View {len(evidence)} supporting source"
                + ("s" if len(evidence) != 1 else "")
            ):

                for source in evidence:

                    title = source.get(
                        "title",
                        "Untitled source"
                    )

                    content = source.get(
                        "content",
                        "No description available."
                    )

                    url = source.get(
                        "url",
                        ""
                    )

                    st.markdown(
                        f"**{title}**"
                    )

                    st.caption(content)

                    if url:

                        st.link_button(
                            "↗ Open source",
                            url
                        )

    st.divider()


# ============================================================
# SUMMARY
# ============================================================

def display_summary(analyzed_claims):

    total = len(analyzed_claims)

    high = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get("confidence") == "HIGH"
    )

    medium = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get("confidence") == "MEDIUM"
    )

    needs_review = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get("confidence")
        in [
            "LOW",
            "SPECULATIVE",
            "PURE GENERATION"
        ]
    )


    st.markdown("### ✦ Confidence Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Claims", total)

    with col2:
        st.metric("High", high)

    with col3:
        st.metric("Medium", medium)

    with col4:
        st.metric("Needs Review", needs_review)


# ============================================================
# FOLLOW-UP PROMPT
# ============================================================

def display_question_prompt():

    st.markdown("### ✦ Keep exploring")

    st.caption(
        "Ask something related to your previous question, "
        "or explore a completely different topic."
    )
