import streamlit as st


# ============================================================
# GLOBAL THEME
# ============================================================

def load_css():

    st.html("""
    <style>

    /* ========================================================
       FONTS
       ======================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800'
        '&family=Sora:wght@400;500;600;700&display=swap'
    );


    /* ========================================================
       MAIN BACKGROUND
       ======================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 0% 0%,
                rgba(0, 210, 190, 0.16),
                transparent 25%
            ),

            radial-gradient(
                circle at 100% 5%,
                rgba(255, 125, 92, 0.13),
                transparent 25%
            ),

            radial-gradient(
                circle at 50% 100%,
                rgba(255, 202, 72, 0.10),
                transparent 30%
            ),

            linear-gradient(
                135deg,
                #F7FCFB 0%,
                #F5FAFC 50%,
                #FFF9F5 100%
            );

        color: #172A35;
    }


    /* ========================================================
       PAGE WIDTH
       ======================================================== */

    .block-container {

        max-width: 900px;

        padding-top: 2.3rem;
        padding-bottom: 4rem;
    }


    /* ========================================================
       GLOBAL FONTS
       ======================================================== */

    html,
    body,
    [class*="css"] {

        font-family: 'Manrope', sans-serif;
    }

    h1,
    h2,
    h3 {

        font-family: 'Sora', sans-serif !important;

        color: #132B36 !important;

        letter-spacing: -0.035em;
    }

    p {

        font-family: 'Manrope', sans-serif !important;

        color: #60737C;
    }


    /* ========================================================
       STREAMLIT CLEANUP
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

        font-family: 'Sora', sans-serif !important;

        font-size: 3.25rem !important;

        font-weight: 700 !important;

        letter-spacing: -0.06em !important;

        background: linear-gradient(
            90deg,
            #00A99D,
            #00B8C8,
            #1688A8
        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }


    /* ========================================================
       INPUT
       ======================================================== */

    .stTextInput > div > div > input {

        background: rgba(255, 255, 255, 0.96) !important;

        color: #172A35 !important;

        border: 1.5px solid rgba(0, 169, 157, 0.22) !important;

        border-radius: 18px !important;

        padding: 0.9rem 1.1rem !important;

        font-family: 'Manrope', sans-serif !important;

        font-size: 1rem !important;

        font-weight: 500 !important;

        box-shadow:
            0 8px 28px rgba(20, 70, 80, 0.07);

        transition: all 0.2s ease;
    }


    .stTextInput > div > div > input:focus {

        border-color: #00A99D !important;

        box-shadow:
            0 0 0 4px rgba(0, 169, 157, 0.10),
            0 12px 32px rgba(20, 70, 80, 0.10);

        outline: none !important;
    }


    .stTextInput > div > div > input::placeholder {

        color: #8A9BA2 !important;
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
            #00A99D 0%,
            #00B8C8 55%,
            #1688A8 100%
        ) !important;

        color: white !important;

        font-family: 'Manrope', sans-serif !important;

        font-size: 0.98rem !important;

        font-weight: 800 !important;

        box-shadow:
            0 10px 24px rgba(0, 157, 165, 0.22);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease;
    }


    .stFormSubmitButton > button:hover,
    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 15px 30px rgba(0, 157, 165, 0.30);
    }


    /* ========================================================
       CONTAINERS / CARDS
       ======================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {

        background: rgba(255, 255, 255, 0.78) !important;

        border: 1px solid rgba(25, 85, 95, 0.10) !important;

        border-radius: 20px !important;

        box-shadow:
            0 10px 30px rgba(30, 65, 75, 0.055);

        backdrop-filter: blur(10px);
    }


    /* ========================================================
       METRICS
       ======================================================== */

    [data-testid="stMetric"] {

        background: rgba(255, 255, 255, 0.80);

        border: 1px solid rgba(0, 169, 157, 0.11);

        border-radius: 18px;

        padding: 1rem;

        box-shadow:
            0 8px 22px rgba(30, 65, 75, 0.05);
    }


    [data-testid="stMetricLabel"] {

        font-family: 'Manrope', sans-serif !important;

        color: #71838B !important;

        font-weight: 600 !important;
    }


    [data-testid="stMetricValue"] {

        font-family: 'Sora', sans-serif !important;

        color: #17333E !important;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    .stExpander {

        background: rgba(250, 253, 253, 0.80) !important;

        border: 1px solid rgba(0, 169, 157, 0.12) !important;

        border-radius: 16px !important;

        box-shadow:
            0 7px 22px rgba(30, 65, 75, 0.04);
    }


    .stExpander summary {

        font-family: 'Manrope', sans-serif !important;

        font-weight: 700 !important;

        color: #29434D !important;
    }


    /* ========================================================
       SUCCESS — HIGH CONFIDENCE
       ======================================================== */

    .stAlert[data-baseweb="notification"] {

        border-radius: 14px !important;

        font-family: 'Manrope', sans-serif !important;
    }


    /* ========================================================
       LINKS
       ======================================================== */

    .stLinkButton > a {

        border-radius: 10px !important;

        border: 1px solid rgba(0, 169, 157, 0.20) !important;

        color: #008D84 !important;

        background: #F0FBF9 !important;

        font-family: 'Manrope', sans-serif !important;

        font-weight: 700 !important;
    }


    .stLinkButton > a:hover {

        background: #E1F7F4 !important;

        border-color: #00A99D !important;
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
            rgba(0, 169, 157, 0.22),
            rgba(255, 125, 92, 0.20),
            transparent
        ) !important;

        margin: 2rem 0 !important;
    }


    /* ========================================================
       SPINNER
       ======================================================== */

    .stSpinner > div {

        border-top-color: #00A99D !important;
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

            font-size: 2.35rem !important;
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

    st.markdown(
        "### ✦ Claim-by-Claim Analysis"
    )

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


    with st.container(border=True):

        st.caption("AI CLAIM")

        st.markdown(
            f"**{claim}**"
        )


        # ----------------------------------------------------
        # HIGH
        # ----------------------------------------------------

        if level == "HIGH":

            st.success(
                "🟢 HIGH CONFIDENCE"
            )


        # ----------------------------------------------------
        # MEDIUM
        # ----------------------------------------------------

        elif level == "MEDIUM":

            st.warning(
                "🟡 MEDIUM CONFIDENCE"
            )


        # ----------------------------------------------------
        # SPECULATIVE
        # ----------------------------------------------------

        elif level in [
            "SPECULATIVE",
            "PURE GENERATION"
        ]:

            st.warning(
                "🟠 SPECULATIVE — Pure Generation"
            )


        # ----------------------------------------------------
        # LOW
        # ----------------------------------------------------

        else:

            st.error(
                "🔴 LOW CONFIDENCE"
            )


        # ----------------------------------------------------
        # REASON
        # ----------------------------------------------------

        st.markdown(
            "**Why this rating?**"
        )

        st.info(reason)


        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        st.markdown(
            "**Supporting Evidence**"
        )


        if not evidence:

            st.warning(
                "No supporting sources were found. "
                "Treat this statement as speculative."
            )


        else:

            with st.expander(
                f"View {len(evidence)} supporting source"
                + (
                    "s"
                    if len(evidence) != 1
                    else ""
                )
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

                    st.caption(
                        content
                    )

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
        if item["confidence"].get(
            "confidence"
        ) == "HIGH"
    )

    medium = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get(
            "confidence"
        ) == "MEDIUM"
    )

    needs_review = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get(
            "confidence"
        ) in [
            "LOW",
            "SPECULATIVE",
            "PURE GENERATION"
        ]
    )


    st.markdown(
        "### ✦ Confidence Overview"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Claims",
            total
        )


    with col2:

        st.metric(
            "High",
            high
        )


    with col3:

        st.metric(
            "Medium",
            medium
        )


    with col4:

        st.metric(
            "Needs Review",
            needs_review
        )


# ============================================================
# FOLLOW-UP PROMPT
# ============================================================

def display_question_prompt():

    st.markdown(
        "### ✦ Keep exploring"
    )

    st.caption(
        "Ask something related to your previous question, "
        "or explore a completely different topic."
    )
