import streamlit as st


# ============================================================
# GLOBAL STYLE
# ============================================================

def load_css():

    st.html("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(132, 92, 230, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 92% 12%,
            rgba(55, 190, 220, 0.15),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(220, 120, 210, 0.10),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #F8F7FF 0%,
            #F3F6FC 48%,
            #EEF9FA 100%
        );
}


/* ------------------------------------------------------------
   MAIN CONTENT
------------------------------------------------------------ */

.block-container {
    max-width: 950px;
    padding-top: 3.5rem;
    padding-bottom: 5rem;
}


/* ------------------------------------------------------------
   HEADINGS
------------------------------------------------------------ */

h1 {
    color: #18233D !important;
    font-family: "Trebuchet MS", Arial, sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: -1px !important;
}

h2 {
    color: #273149 !important;
    font-family: "Trebuchet MS", Arial, sans-serif !important;
    font-weight: 750 !important;
}

h3 {
    color: #303B56 !important;
    font-family: "Trebuchet MS", Arial, sans-serif !important;
}

p {
    color: #4E5A72;
}


/* ------------------------------------------------------------
   TEXT INPUT
------------------------------------------------------------ */

div[data-testid="stTextInput"] {
    margin-top: 8px;
    margin-bottom: 10px;
}

div[data-testid="stTextInput"] input {

    background-color: #FFFFFF !important;

    color: #18233D !important;

    caret-color: #7655E8 !important;

    border: 2px solid #D8DDEA !important;

    border-radius: 16px !important;

    padding: 15px 18px !important;

    font-family:
        "Trebuchet MS",
        Arial,
        sans-serif !important;

    font-size: 16px !important;

    font-weight: 600 !important;

    box-shadow:
        0 8px 25px
        rgba(50, 60, 100, 0.08) !important;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease !important;
}


div[data-testid="stTextInput"] input:focus {

    background-color: #FFFFFF !important;

    color: #18233D !important;

    border-color: #7655E8 !important;

    box-shadow:
        0 0 0 4px
        rgba(118, 85, 232, 0.12),
        0 10px 28px
        rgba(60, 70, 110, 0.10) !important;
}


div[data-testid="stTextInput"] input::placeholder {

    color: #8A94A8 !important;

    opacity: 1 !important;
}


/* ------------------------------------------------------------
   ANALYZE BUTTON
------------------------------------------------------------ */

div[data-testid="stFormSubmitButton"] button {

    background:
        linear-gradient(
            135deg,
            #7655E8,
            #4F8DDE
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    font-family:
        "Trebuchet MS",
        Arial,
        sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    padding: 11px 24px !important;

    min-height: 44px !important;

    box-shadow:
        0 8px 22px
        rgba(90, 75, 200, 0.22) !important;

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease !important;
}


div[data-testid="stFormSubmitButton"] button:hover {

    background:
        linear-gradient(
            135deg,
            #6847D8,
            #3D7FD2
        ) !important;

    color: #FFFFFF !important;

    transform: translateY(-1px) !important;

    box-shadow:
        0 11px 27px
        rgba(90, 75, 200, 0.30) !important;
}


/* ------------------------------------------------------------
   EXPANDERS
------------------------------------------------------------ */

div[data-testid="stExpander"] {

    background:
        rgba(255, 255, 255, 0.82) !important;

    border:
        1px solid #DDE3EF !important;

    border-radius:
        16px !important;

    box-shadow:
        0 6px 20px
        rgba(40, 50, 90, 0.05) !important;
}


div[data-testid="stExpander"] summary {

    color: #35415C !important;

    font-family:
        "Trebuchet MS",
        Arial,
        sans-serif !important;

    font-weight: 700 !important;
}


/* ------------------------------------------------------------
   SUCCESS
------------------------------------------------------------ */

div[data-testid="stAlert"] {

    border-radius: 14px !important;

    font-family:
        "Trebuchet MS",
        Arial,
        sans-serif !important;
}


/* ------------------------------------------------------------
   METRICS
------------------------------------------------------------ */

div[data-testid="stMetric"] {

    background:
        rgba(255, 255, 255, 0.75);

    border:
        1px solid #E0E4EF;

    border-radius:
        16px;

    padding:
        12px 14px;

    box-shadow:
        0 6px 18px
        rgba(40, 50, 90, 0.05);
}


div[data-testid="stMetricLabel"] {

    color: #7A849A !important;

    font-weight: 600 !important;
}


div[data-testid="stMetricValue"] {

    color: #273149 !important;

    font-weight: 800 !important;
}


/* ------------------------------------------------------------
   DIVIDERS
------------------------------------------------------------ */

hr {

    border: none !important;

    height: 1px !important;

    background:
        linear-gradient(
            90deg,
            transparent,
            #D8DDEA,
            transparent
        ) !important;

    margin-top: 25px !important;

    margin-bottom: 25px !important;
}


/* ------------------------------------------------------------
   CAPTIONS
------------------------------------------------------------ */

[data-testid="stCaptionContainer"] {

    color: #7B8499 !important;
}


/* ------------------------------------------------------------
   SPINNER
------------------------------------------------------------ */

div[data-testid="stSpinner"] {

    color: #6650C9 !important;
}

</style>
""")


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown(
        "# 🧠 AI Confidence Layer"
    )

    st.markdown(
        "### Don't just get an AI answer."
    )

    st.markdown(
        "#### Understand **why you should trust it.**"
    )

    st.caption(
        "Evidence  •  Claim Analysis  •  Trust Signals"
    )

    st.divider()


# ============================================================
# FIRST QUESTION
# ============================================================

def display_first_question():

    st.markdown(
        "## What would you like to know?"
    )

    st.caption(
        "Ask a question and we'll help you understand "
        "how much you can trust the answer."
    )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown(
        "## 🔬 Claim-by-Claim Analysis"
    )

    st.caption(
        "See how each part of the AI answer is supported."
    )


# ============================================================
# CLAIM DISPLAY
# ============================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get(
        "confidence",
        "LOW"
    )

    reason = confidence.get(
        "reason",
        "There is not enough evidence to determine this claim."
    )


    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    if level == "HIGH":

        st.success(
            "🟢 STRONGLY SUPPORTED"
        )

    elif level == "MEDIUM":

        st.warning(
            "🟡 PARTIALLY SUPPORTED"
        )

    else:

        st.info(
            "🟠 PURE GENERATION · SPECULATIVE"
        )


    # --------------------------------------------------------
    # CLAIM
    # --------------------------------------------------------

    st.markdown(
        f"### {claim}"
    )


    # --------------------------------------------------------
    # REASON
    # --------------------------------------------------------

    st.markdown(
        "**Why this rating?**"
    )

    st.write(
        reason
    )


    # --------------------------------------------------------
    # EVIDENCE
    # --------------------------------------------------------

    with st.expander(
        "▸ View Supporting Evidence"
    ):

        if not evidence:

            st.info(
                "🟠 Pure Generation / Speculative\n\n"
                "No retrieved source was found for this claim. "
                "Treat this information cautiously."
            )

        else:

            for source in evidence:

                title = source.get(
                    "title",
                    "Source"
                )

                content = source.get(
                    "content",
                    "No content available."
                )

                url = source.get(
                    "url",
                    ""
                )

                st.markdown(
                    f"#### ◈ {title}"
                )

                st.write(
                    content
                )

                if url:

                    st.link_button(
                        "Open source ↗",
                        url
                    )

                st.divider()


    st.divider()


# ============================================================
# TRUST SUMMARY
# ============================================================

def display_summary(analyzed_claims):

    total = len(
        analyzed_claims
    )

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

    low = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get("confidence") == "LOW"
    )


    st.markdown(
        "## ✦ Trust Overview"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Claims",
            total
        )


    with col2:

        st.metric(
            "Strong",
            high
        )


    with col3:

        st.metric(
            "Partial",
            medium
        )


    with col4:

        st.metric(
            "Speculative",
            low
        )


# ============================================================
# FOLLOW-UP PROMPT
# ============================================================

def display_question_prompt():

    st.divider()

    st.markdown(
        "## ✨ What would you like to know next?"
    )

    st.caption(
        "Ask something related to your previous question "
        "or explore a completely different topic."
    )
