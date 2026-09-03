import streamlit as st


# ============================================================
# GLOBAL THEME
# ============================================================

def load_css():

    st.html("""
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800'
    '&family=Space+Grotesk:wght@400;500;600;700&display=swap'
);


/* ============================================================
   APP BACKGROUND
   ============================================================ */

.stApp {

    background:

        radial-gradient(
            circle at 5% 0%,
            rgba(79, 125, 255, 0.12),
            transparent 25%
        ),

        radial-gradient(
            circle at 96% 8%,
            rgba(255, 122, 112, 0.11),
            transparent 23%
        ),

        radial-gradient(
            circle at 45% 100%,
            rgba(91, 220, 169, 0.10),
            transparent 28%
        ),

        #F8F9FC;

    color: #172033;
}


/* ============================================================
   PAGE WIDTH
   ============================================================ */

.block-container {

    max-width: 920px;

    padding-top: 2.5rem;
    padding-bottom: 5rem;
}


/* ============================================================
   TYPOGRAPHY
   ============================================================ */

html,
body,
[class*="css"] {

    font-family:
        'DM Sans',
        sans-serif;
}


h1,
h2,
h3 {

    font-family:
        'Space Grotesk',
        sans-serif !important;

    color:
        #172033 !important;

    letter-spacing:
        -0.045em;
}


p {

    font-family:
        'DM Sans',
        sans-serif !important;

    color:
        #667085;

    line-height:
        1.65;
}


/* ============================================================
   HIDE STREAMLIT BRANDING
   ============================================================ */

#MainMenu {

    visibility:
        hidden;
}


footer {

    visibility:
        hidden;
}


header {

    background:
        transparent !important;
}


/* ============================================================
   MAIN TITLE
   ============================================================ */

[data-testid="stHeading"] h1 {

    font-family:
        'Space Grotesk',
        sans-serif !important;

    font-size:
        3.15rem !important;

    font-weight:
        700 !important;

    letter-spacing:
        -0.065em !important;

    background:

        linear-gradient(
            100deg,
            #3159D8 0%,
            #4378F4 45%,
            #E96B72 100%
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;
}


/* ============================================================
   HEADINGS
   ============================================================ */

h2 {

    font-size:
        1.7rem !important;
}


h3 {

    font-size:
        1.35rem !important;
}


/* ============================================================
   TEXT INPUT
   ============================================================ */

.stTextInput > div > div > input {

    background:
        rgba(255, 255, 255, 0.96) !important;

    color:
        #172033 !important;

    border:
        1.5px solid #D9DFEA !important;

    border-radius:
        18px !important;

    min-height:
        54px !important;

    padding:
        0.9rem 1.15rem !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-size:
        1rem !important;

    font-weight:
        500 !important;

    box-shadow:

        0 8px 25px
        rgba(35, 55, 90, 0.06);

    transition:
        all 0.2s ease;
}


.stTextInput > div > div > input:focus {

    border-color:
        #4674E8 !important;

    box-shadow:

        0 0 0 4px
        rgba(70, 116, 232, 0.10),

        0 12px 30px
        rgba(35, 55, 90, 0.08);

    outline:
        none !important;
}


.stTextInput > div > div > input::placeholder {

    color:
        #98A2B3 !important;
}


/* ============================================================
   PRIMARY BUTTON
   ============================================================ */

.stFormSubmitButton > button {

    width:
        100%;

    min-height:
        52px;

    border:
        none !important;

    border-radius:
        15px !important;

    background:

        linear-gradient(
            100deg,
            #3159D8,
            #4678ED
        ) !important;

    color:
        #FFFFFF !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-size:
        0.98rem !important;

    font-weight:
        700 !important;

    box-shadow:

        0 10px 25px
        rgba(49, 89, 216, 0.22);

    transition:
        all 0.2s ease;
}


.stFormSubmitButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:

        0 14px 32px
        rgba(49, 89, 216, 0.28);
}


/* ============================================================
   SECONDARY BUTTONS
   ============================================================ */

.stButton > button {

    background:
        rgba(255, 255, 255, 0.86) !important;

    color:
        #3159D8 !important;

    border:
        1px solid #DCE3F0 !important;

    border-radius:
        13px !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-weight:
        600 !important;

    transition:
        all 0.18s ease;
}


.stButton > button:hover {

    background:
        #EEF3FF !important;

    border-color:
        #9DB4F4 !important;

    transform:
        translateY(-1px);
}


/* ============================================================
   CARDS
   ============================================================ */

[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        rgba(255, 255, 255, 0.88) !important;

    border:
        1px solid #E5E9F1 !important;

    border-radius:
        21px !important;

    box-shadow:

        0 12px 35px
        rgba(38, 54, 83, 0.055);

    backdrop-filter:
        blur(12px);
}


/* ============================================================
   CLAIM CARD HOVER
   ============================================================ */

[data-testid="stVerticalBlockBorderWrapper"]:hover {

    border-color:
        #D4DCEF !important;

    box-shadow:

        0 15px 40px
        rgba(38, 54, 83, 0.08);
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

[data-testid="stMetric"] {

    background:
        rgba(255, 255, 255, 0.92);

    border:
        1px solid #E4E8F0;

    border-radius:
        17px;

    padding:
        1rem;

    box-shadow:

        0 7px 22px
        rgba(38, 54, 83, 0.045);
}


[data-testid="stMetricLabel"] {

    color:
        #7A8496 !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-weight:
        600 !important;
}


[data-testid="stMetricValue"] {

    color:
        #172033 !important;

    font-family:
        'Space Grotesk',
        sans-serif !important;
}


/* ============================================================
   EXPANDERS
   ============================================================ */

.stExpander {

    background:
        rgba(255, 255, 255, 0.72) !important;

    border:
        1px solid #E2E7EF !important;

    border-radius:
        16px !important;
}


.stExpander summary {

    color:
        #344054 !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-weight:
        700 !important;
}


/* ============================================================
   HIGH CONFIDENCE — MINT
   ============================================================ */

.stSuccess {

    background:
        #ECFBF4 !important;

    border:
        1px solid #B9EBD1 !important;

    border-left:
        4px solid #35B879 !important;

    color:
        #176B48 !important;

    border-radius:
        13px !important;
}


/* ============================================================
   MEDIUM CONFIDENCE — APRICOT
   ============================================================ */

.stWarning {

    background:
        #FFF7E9 !important;

    border:
        1px solid #F5D9A3 !important;

    border-left:
        4px solid #F2A93B !important;

    color:
        #875A17 !important;

    border-radius:
        13px !important;
}


/* ============================================================
   LOW CONFIDENCE — CORAL
   ============================================================ */

.stError {

    background:
        #FFF0F1 !important;

    border:
        1px solid #F3C2C6 !important;

    border-left:
        4px solid #E96B72 !important;

    color:
        #913B42 !important;

    border-radius:
        13px !important;
}


/* ============================================================
   INFORMATION — BLUE
   ============================================================ */

.stInfo {

    background:
        #EEF4FF !important;

    border:
        1px solid #C9D8FA !important;

    border-left:
        4px solid #4678ED !important;

    color:
        #294A9B !important;

    border-radius:
        13px !important;
}


/* ============================================================
   SOURCE LINKS
   ============================================================ */

.stLinkButton > a {

    background:
        #F4F7FF !important;

    border:
        1px solid #D6E0F7 !important;

    color:
        #3159D8 !important;

    border-radius:
        10px !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-weight:
        700 !important;
}


.stLinkButton > a:hover {

    background:
        #EAF0FF !important;

    border-color:
        #9EB5F2 !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {

    border:
        none !important;

    height:
        1px !important;

    background:

        linear-gradient(
            90deg,
            transparent,
            #D8DFEC,
            #F0B6B9,
            #D8DFEC,
            transparent
        ) !important;

    margin:
        2.2rem 0 !important;
}


/* ============================================================
   SPINNER
   ============================================================ */

.stSpinner > div {

    border-top-color:
        #4674E8 !important;
}


/* ============================================================
   CAPTIONS
   ============================================================ */

[data-testid="stCaptionContainer"] {

    color:
        #7A8496 !important;

    font-family:
        'DM Sans',
        sans-serif !important;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .block-container {

        padding-left:
            1rem;

        padding-right:
            1rem;
    }


    [data-testid="stHeading"] h1 {

        font-size:
            2.35rem !important;
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
        "### What are you curious about?"
    )

    st.caption(
        "Ask anything. We'll break the answer down, "
        "check the evidence, and show you what deserves trust."
    )


# ============================================================
# QUICK QUESTIONS
# ============================================================

def display_quick_questions():

    st.markdown(
        "### ✦ Start exploring"
    )

    st.caption(
        "Try one of these questions to see the confidence layer."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "🔬 Try a science question",
            key="quick_science",
            use_container_width=True
        )

        st.button(
            "🌎 Explore a historical fact",
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
            "💭 Ask something unexpected",
            key="quick_unexpected",
            use_container_width=True
        )


# ============================================================
# QUESTION
# ============================================================

def display_question(question):

    st.markdown(
        "### Your question"
    )

    with st.container(border=True):

        st.markdown(
            f"**{question}**"
        )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown(
        "### ✦ Claim-by-claim analysis"
    )

    st.caption(
        "Every factual statement is checked against external evidence."
    )


# ============================================================
# CLAIM
# ============================================================

def display_claim(
    claim,
    confidence,
    evidence
):

    level = confidence.get(
        "confidence",
        "LOW"
    ).upper()

    reason = confidence.get(
        "reason",
        "There is not enough evidence to determine reliability."
    )


    with st.container(border=True):

        st.caption(
            "AI CLAIM"
        )

        st.markdown(
            f"**{claim}**"
        )


        # ----------------------------------------------------
        # CONFIDENCE
        # ----------------------------------------------------

        if level == "HIGH":

            st.success(
                "✓  HIGH CONFIDENCE · Strongly supported"
            )

        elif level == "MEDIUM":

            st.warning(
                "◐  MEDIUM CONFIDENCE · Partially supported"
            )

        elif level in [
            "SPECULATIVE",
            "PURE GENERATION"
        ]:

            st.warning(
                "◌  SPECULATIVE · Limited external evidence"
            )

        else:

            st.error(
                "×  LOW CONFIDENCE · Needs verification"
            )


        # ----------------------------------------------------
        # REASON
        # ----------------------------------------------------

        st.markdown(
            "**Why this rating?**"
        )

        st.info(
            reason
        )


        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        st.markdown(
            "**Supporting evidence**"
        )


        if not evidence:

            st.warning(
                "No supporting sources were found. "
                "Treat this statement as speculative."
            )

        else:

            source_count = len(evidence)

            st.caption(
                f"◈ {source_count} source"
                + (
                    "s found"
                    if source_count != 1
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
                            "↗  Open source",
                            url
                        )


    st.divider()


# ============================================================
# SUMMARY
# ============================================================

def display_summary(analyzed_claims):

    total = len(
        analyzed_claims
    )


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
        "### ✦ Confidence overview"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Claims",
            total
        )


    with col2:

        st.metric(
            "✓ Strong",
            high
        )


    with col3:

        st.metric(
            "◐ Partial",
            medium
        )


    with col4:

        st.metric(
            "⚠ Review",
            needs_review
        )


# ============================================================
# HOW IT WORKS
# ============================================================

def display_how_it_works():

    with st.expander(
        "◎ How does the Confidence Layer work?"
    ):

        st.markdown(
            """
            **01 · Generate**

            The AI creates a natural answer to your question.

            **02 · Break it down**

            The answer is separated into individual factual claims.

            **03 · Find evidence**

            Each claim is checked against external sources.

            **04 · Evaluate**

            The evidence is compared with the claim.

            **05 · Explain**

            You see the confidence level and the reasoning behind it.
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
        "or explore something completely different."
    )


# ============================================================
# CLEAR CONVERSATION
# ============================================================

def display_clear_button():

    if st.button(
        "↺  Start a new conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()
