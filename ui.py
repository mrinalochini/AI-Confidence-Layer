import streamlit as st


# ============================================================
# GLOBAL THEME
# ============================================================

def load_css():

    st.html("""
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800'
        '&family=Sora:wght@400;500;600;700&display=swap'
    );


    /* ========================================================
       BACKGROUND
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
                rgba(255, 125, 92, 0.14),
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
       LAYOUT
       ======================================================== */

    .block-container {

        max-width: 900px;

        padding-top: 2.3rem;

        padding-bottom: 4rem;
    }


    /* ========================================================
       FONTS
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
       HIDE STREAMLIT UI
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
       TITLE
       ======================================================== */

    [data-testid="stHeading"] h1 {

        font-family: 'Sora', sans-serif !important;

        font-size: 3.2rem !important;

        font-weight: 700 !important;

        letter-spacing: -0.06em !important;

        background: linear-gradient(
            90deg,
            #009F91,
            #00B8C8,
            #197FA0
        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }


    /* ========================================================
       INPUT
       ======================================================== */

    .stTextInput > div > div > input {

        background: rgba(255, 255, 255, 0.97) !important;

        color: #172A35 !important;

        border: 1.5px solid rgba(0, 169, 157, 0.24) !important;

        border-radius: 18px !important;

        padding: 0.9rem 1.1rem !important;

        font-family: 'Manrope', sans-serif !important;

        font-size: 1rem !important;

        font-weight: 500 !important;

        box-shadow:
            0 8px 28px rgba(20, 70, 80, 0.07);
    }


    .stTextInput > div > div > input:focus {

        border-color: #00A99D !important;

        box-shadow:
            0 0 0 4px rgba(0, 169, 157, 0.10),
            0 12px 32px rgba(20, 70, 80, 0.10);
    }


    .stTextInput > div > div > input::placeholder {

        color: #8A9BA2 !important;
    }


    /* ========================================================
       MAIN BUTTON
       ======================================================== */

    .stFormSubmitButton > button {

        width: 100%;

        min-height: 48px;

        border: none !important;

        border-radius: 15px !important;

        background: linear-gradient(
            135deg,
            #00A99D,
            #00B8C8,
            #1688A8
        ) !important;

        color: white !important;

        font-family: 'Manrope', sans-serif !important;

        font-size: 0.98rem !important;

        font-weight: 800 !important;

        box-shadow:
            0 10px 24px rgba(0, 157, 165, 0.22);
    }


    .stFormSubmitButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 15px 30px rgba(0, 157, 165, 0.30);
    }


    /* ========================================================
       NORMAL BUTTONS
       ======================================================== */

    .stButton > button {

        border-radius: 13px !important;

        border: 1px solid rgba(0, 169, 157, 0.20) !important;

        background: rgba(255, 255, 255, 0.80) !important;

        color: #087F78 !important;

        font-family: 'Manrope', sans-serif !important;

        font-weight: 700 !important;

        transition: all 0.18s ease;
    }


    .stButton > button:hover {

        background: #E8FAF7 !important;

        border-color: #00A99D !important;

        transform: translateY(-1px);
    }


    /* ========================================================
       CARDS
       ======================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {

        background: rgba(255, 255, 255, 0.82) !important;

        border: 1px solid rgba(25, 85, 95, 0.10) !important;

        border-radius: 20px !important;

        box-shadow:
            0 10px 30px rgba(30, 65, 75, 0.055);
    }


    /* ========================================================
       METRICS
       ======================================================== */

    [data-testid="stMetric"] {

        background: rgba(255, 255, 255, 0.82);

        border: 1px solid rgba(0, 169, 157, 0.12);

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

        background: rgba(250, 253, 253, 0.82) !important;

        border: 1px solid rgba(0, 169, 157, 0.13) !important;

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


    /* ========================================================
       ALERTS
       ======================================================== */

    .stAlert {

        border-radius: 14px !important;

        font-family: 'Manrope', sans-serif !important;
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
        "Ask naturally. We'll break the answer down and show "
        "you what the evidence actually supports."
    )


# ============================================================
# QUICK START
# ============================================================

def display_quick_questions():

    st.markdown("### ⚡ Try something")

    st.caption(
        "Not sure what to ask? Start with one of these."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "🔬 Ask a science question",
            key="quick_science",
            use_container_width=True
        )

        st.button(
            "🌍 Ask about history",
            key="quick_history",
            use_container_width=True
        )

    with col2:

        st.button(
            "🤖 Test an AI claim",
            key="quick_ai",
            use_container_width=True
        )

        st.button(
            "🧠 Challenge a fact",
            key="quick_fact",
            use_container_width=True
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
        "We check each factual statement against retrieved evidence."
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


        if level == "HIGH":

            st.success(
                "🟢 HIGH CONFIDENCE · Strongly supported"
            )

        elif level == "MEDIUM":

            st.warning(
                "🟡 MEDIUM CONFIDENCE · Partially supported"
            )

        elif level in [
            "SPECULATIVE",
            "PURE GENERATION"
        ]:

            st.warning(
                "🟠 SPECULATIVE · Little or no external evidence"
            )

        else:

            st.error(
                "🔴 LOW CONFIDENCE · Needs verification"
            )


        st.markdown(
            "**Why this rating?**"
        )

        st.info(reason)


        st.markdown(
            "**Supporting Evidence**"
        )


        if not evidence:

            st.warning(
                "No supporting sources were found. "
                "Treat this statement as speculative."
            )

        else:

            st.caption(
                f"🔎 {len(evidence)} source"
                + (
                    "s found"
                    if len(evidence) != 1
                    else " found"
                )
            )


            with st.expander(
                "View supporting evidence"
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
            "🟢 Strong",
            high
        )


    with col3:

        st.metric(
            "🟡 Partial",
            medium
        )


    with col4:

        st.metric(
            "🟠 Review",
            needs_review
        )


# ============================================================
# HOW IT WORKS
# ============================================================

def display_how_it_works():

    with st.expander(
        "🧭 How does AI Confidence Layer work?"
    ):

        st.markdown(
            """
            **01 · Generate**

            The AI creates a natural-language answer to your question.

            **02 · Break down**

            The answer is separated into individual factual claims.

            **03 · Find evidence**

            Each claim is checked against external sources.

            **04 · Evaluate**

            The evidence is compared with the claim.

            **05 · Explain**

            You see not only a confidence level, but *why*
            that level was assigned.
            """
        )


# ============================================================
# FOLLOW-UP
# ============================================================

def display_question_prompt():

    st.markdown(
        "### ✦ Keep exploring"
    )

    st.caption(
        "Ask a follow-up, challenge the answer, "
        "or switch to a completely different topic."
    )


# ============================================================
# CLEAR CONVERSATION
# ============================================================

def display_clear_button():

    if st.button(
        "🧹 Clear conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()
