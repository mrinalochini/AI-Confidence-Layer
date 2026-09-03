import streamlit as st


# ============================================================
# GLOBAL THEME
# ============================================================

def load_css():
    st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');


/* ============================================================
   GLOBAL APP
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(124, 92, 255, 0.18),
            transparent 25%
        ),
        radial-gradient(
            circle at 95% 10%,
            rgba(0, 207, 255, 0.16),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(255, 92, 205, 0.10),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #F8F7FF 0%,
            #F4F7FF 45%,
            #F0FBFC 100%
        );

    color: #172033;
    font-family: 'DM Sans', sans-serif;
}


/* Main content width */

.block-container {
    max-width: 900px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}


/* ============================================================
   REMOVE STREAMLIT DECORATIONS
   ============================================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* ============================================================
   TYPOGRAPHY
   ============================================================ */

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #151A33 !important;
    letter-spacing: -0.035em;
}

p, label, .stMarkdown {
    font-family: 'DM Sans', sans-serif;
}

h1 {
    font-weight: 700 !important;
}

h2 {
    font-weight: 600 !important;
}

h3 {
    font-weight: 600 !important;
}


/* ============================================================
   HEADER
   ============================================================ */

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.2rem;
    font-weight: 700;
    letter-spacing: -0.06em;

    background: linear-gradient(
        90deg,
        #6C45F5,
        #8B5CF6,
        #08AEEA
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0.35rem;
}

.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.15rem;
    font-weight: 500;
    color: #65708A;
    margin-bottom: 2rem;
}

.hero-line {
    height: 4px;
    width: 85px;

    background: linear-gradient(
        90deg,
        #7655E8,
        #00B8D9
    );

    border-radius: 50px;
    margin-bottom: 1.8rem;
}


/* ============================================================
   QUESTION INPUT
   ============================================================ */

.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.92) !important;

    color: #18233D !important;

    border: 1.5px solid rgba(118, 85, 232, 0.20) !important;

    border-radius: 18px !important;

    padding: 0.85rem 1.1rem !important;

    font-family: 'DM Sans', sans-serif !important;

    font-size: 1rem !important;

    box-shadow:
        0 8px 30px rgba(74, 57, 140, 0.07);

    transition: all 0.2s ease;
}

.stTextInput > div > div > input:focus {
    border: 1.5px solid #7655E8 !important;

    box-shadow:
        0 0 0 4px rgba(118, 85, 232, 0.10),
        0 12px 35px rgba(74, 57, 140, 0.10);

    outline: none !important;
}

.stTextInput > div > div > input::placeholder {
    color: #98A0B5 !important;
}


/* ============================================================
   ANALYZE BUTTON
   ============================================================ */

.stButton > button,
.stFormSubmitButton > button {
    width: 100%;

    min-height: 48px;

    border: none !important;

    border-radius: 15px !important;

    background: linear-gradient(
        135deg,
        #7048F5 0%,
        #5B6CFF 55%,
        #00B8D9 100%
    ) !important;

    color: white !important;

    font-family: 'DM Sans', sans-serif !important;

    font-weight: 700 !important;

    font-size: 0.98rem !important;

    box-shadow:
        0 10px 25px rgba(99, 79, 230, 0.22);

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 15px 32px rgba(99, 79, 230, 0.30);
}


/* ============================================================
   QUESTION CARD
   ============================================================ */

.question-card {
    background: rgba(255, 255, 255, 0.78);

    border: 1px solid rgba(118, 85, 232, 0.12);

    border-radius: 22px;

    padding: 1.3rem 1.5rem;

    margin: 1.3rem 0 2rem;

    box-shadow:
        0 12px 35px rgba(39, 48, 85, 0.06);

    backdrop-filter: blur(14px);
}

.question-label {
    font-family: 'DM Sans', sans-serif;

    font-size: 0.78rem;

    font-weight: 700;

    letter-spacing: 0.10em;

    text-transform: uppercase;

    color: #7655E8;

    margin-bottom: 0.45rem;
}

.question-text {
    font-family: 'Space Grotesk', sans-serif;

    font-size: 1.18rem;

    font-weight: 500;

    line-height: 1.55;

    color: #1A2340;
}


/* ============================================================
   ANALYSIS HEADER
   ============================================================ */

.analysis-title {
    font-family: 'Space Grotesk', sans-serif;

    font-size: 1.55rem;

    font-weight: 700;

    color: #17203B;

    margin-top: 1rem;

    margin-bottom: 0.3rem;
}

.analysis-subtitle {
    font-family: 'DM Sans', sans-serif;

    color: #7A849B;

    font-size: 0.94rem;

    margin-bottom: 1.4rem;
}


/* ============================================================
   CLAIM CARD
   ============================================================ */

.claim-card {
    background: rgba(255, 255, 255, 0.86);

    border-radius: 22px;

    padding: 1.35rem 1.5rem;

    margin: 1rem 0;

    border: 1px solid rgba(96, 81, 190, 0.11);

    box-shadow:
        0 12px 32px rgba(40, 50, 90, 0.07);

    backdrop-filter: blur(12px);
}

.claim-number {
    font-family: 'Space Grotesk', sans-serif;

    font-size: 0.76rem;

    font-weight: 700;

    color: #7655E8;

    letter-spacing: 0.09em;

    text-transform: uppercase;

    margin-bottom: 0.6rem;
}

.claim-text {
    font-family: 'DM Sans', sans-serif;

    font-size: 1.04rem;

    line-height: 1.65;

    color: #202A43;

    font-weight: 500;
}


/* ============================================================
   CONFIDENCE BADGES
   ============================================================ */

.confidence-high {
    display: inline-block;

    background: #E6FAF1;

    color: #087443;

    border: 1px solid #B9EED8;

    border-radius: 50px;

    padding: 0.42rem 0.75rem;

    font-family: 'DM Sans', sans-serif;

    font-size: 0.76rem;

    font-weight: 800;

    letter-spacing: 0.05em;
}


.confidence-medium {
    display: inline-block;

    background: #FFF6D9;

    color: #9A6500;

    border: 1px solid #F2D98A;

    border-radius: 50px;

    padding: 0.42rem 0.75rem;

    font-family: 'DM Sans', sans-serif;

    font-size: 0.76rem;

    font-weight: 800;

    letter-spacing: 0.05em;
}


.confidence-speculative {
    display: inline-block;

    background: #FFF1D6;

    color: #9B5B00;

    border: 1px dashed #E4A63A;

    border-radius: 50px;

    padding: 0.42rem 0.75rem;

    font-family: 'DM Sans', sans-serif;

    font-size: 0.76rem;

    font-weight: 800;

    letter-spacing: 0.05em;
}


.confidence-low {
    display: inline-block;

    background: #FFE8EC;

    color: #B42345;

    border: 1px solid #F4B8C5;

    border-radius: 50px;

    padding: 0.42rem 0.75rem;

    font-family: 'DM Sans', sans-serif;

    font-size: 0.76rem;

    font-weight: 800;

    letter-spacing: 0.05em;
}


/* ============================================================
   REASON / WHY SECTION
   ============================================================ */

.reason-box {
    background: #F7F5FF;

    border-left: 4px solid #7655E8;

    border-radius: 0 13px 13px 0;

    padding: 0.8rem 1rem;

    margin-top: 1rem;

    color: #59637B;

    font-family: 'DM Sans', sans-serif;

    font-size: 0.91rem;

    line-height: 1.55;
}


/* ============================================================
   EVIDENCE AREA
   ============================================================ */

.evidence-title {
    font-family: 'Space Grotesk', sans-serif;

    font-weight: 700;

    color: #283252;

    font-size: 0.98rem;

    margin-top: 1.2rem;

    margin-bottom: 0.6rem;
}


/* Streamlit expander */

.stExpander {

    border: 1px solid rgba(118, 85, 232, 0.12) !important;

    border-radius: 16px !important;

    background: rgba(248, 248, 255, 0.72) !important;

    box-shadow:
        0 7px 22px rgba(45, 54, 90, 0.04);
}

.stExpander details summary {

    font-family: 'DM Sans', sans-serif !important;

    font-weight: 700 !important;

    color: #3C4562 !important;
}


/* ============================================================
   SOURCE CARDS
   ============================================================ */

.source-card {
    background: white;

    border: 1px solid #E8EAF3;

    border-radius: 15px;

    padding: 1rem;

    margin: 0.75rem 0;

    box-shadow:
        0 5px 18px rgba(40, 48, 80, 0.045);
}

.source-title {
    font-family: 'Space Grotesk', sans-serif;

    font-size: 0.98rem;

    font-weight: 600;

    color: #26304C;

    margin-bottom: 0.45rem;
}

.source-content {
    font-family: 'DM Sans', sans-serif;

    font-size: 0.87rem;

    line-height: 1.55;

    color: #68738A;
}


/* ============================================================
   LINK BUTTONS
   ============================================================ */

.stLinkButton > a {
    border-radius: 10px !important;

    border: 1px solid rgba(118, 85, 232, 0.20) !important;

    color: #6849D9 !important;

    background: #F7F4FF !important;

    font-family: 'DM Sans', sans-serif !important;

    font-weight: 700 !important;

    transition: all 0.18s ease;
}

.stLinkButton > a:hover {
    background: #EEE9FF !important;

    border-color: #7655E8 !important;
}


/* ============================================================
   SUMMARY METRICS
   ============================================================ */

[data-testid="stMetric"] {

    background: rgba(255, 255, 255, 0.76);

    border: 1px solid rgba(118, 85, 232, 0.10);

    border-radius: 18px;

    padding: 1rem;

    box-shadow:
        0 8px 25px rgba(40, 50, 90, 0.05);
}

[data-testid="stMetricLabel"] {
    font-family: 'DM Sans', sans-serif !important;

    color: #707A91 !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;

    color: #252D49 !important;
}


/* ============================================================
   ALERTS
   ============================================================ */

.stAlert {
    border-radius: 15px !important;

    font-family: 'DM Sans', sans-serif !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

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


/* ============================================================
   SPINNER
   ============================================================ */

.stSpinner > div {
    border-top-color: #7655E8 !important;
}


/* ============================================================
   SMALL TEXT
   ============================================================ */

.small-muted {
    font-family: 'DM Sans', sans-serif;

    color: #8A93A7;

    font-size: 0.85rem;
}


/* ============================================================
   FOLLOW-UP PROMPT
   ============================================================ */

.followup-title {
    font-family: 'Space Grotesk', sans-serif;

    font-size: 1.25rem;

    font-weight: 700;

    color: #27304D;

    margin-top: 2.5rem;
}

.followup-text {
    font-family: 'DM Sans', sans-serif;

    color: #788298;

    font-size: 0.92rem;

    margin-bottom: 1rem;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-title {
        font-size: 2.35rem;
    }

    .hero-subtitle {
        font-size: 1rem;
    }

    .claim-card {
        padding: 1.1rem;
    }

}

</style>
""")


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown(
        """
        <div class="hero-title">
            🧠 AI Confidence Layer
        </div>

        <div class="hero-line"></div>

        <div class="hero-subtitle">
            Don't just get an AI answer.<br>
            <b>Understand why you should trust it.</b>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FIRST QUESTION
# ============================================================

def display_first_question():

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:1rem;
            margin-bottom:1.2rem;
        ">
            <div style="
                font-family:'Space Grotesk', sans-serif;
                font-size:1.25rem;
                font-weight:600;
                color:#303954;
            ">
                What would you like to know?
            </div>

            <div style="
                font-family:'DM Sans', sans-serif;
                font-size:0.9rem;
                color:#818AA0;
                margin-top:0.35rem;
            ">
                Ask anything and we'll show you how trustworthy the answer is.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# QUESTION DISPLAY
# ============================================================

def display_question(question):

    st.markdown(
        f"""
        <div class="question-card">

            <div class="question-label">
                Your Question
            </div>

            <div class="question-text">
                {question}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown(
        """
        <div class="analysis-title">
            Claim-by-Claim Analysis
        </div>

        <div class="analysis-subtitle">
            Each statement is evaluated against retrieved evidence.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CLAIM
# ============================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get("confidence", "LOW").upper()

    if level == "HIGH":

        badge_class = "confidence-high"
        badge_text = "● HIGH CONFIDENCE"

    elif level == "MEDIUM":

        badge_class = "confidence-medium"
        badge_text = "● MEDIUM CONFIDENCE"

    elif level in ["SPECULATIVE", "PURE GENERATION"]:

        badge_class = "confidence-speculative"
        badge_text = "◌ SPECULATIVE"

    else:

        badge_class = "confidence-low"
        badge_text = "● LOW CONFIDENCE"


    # Claim card

    st.markdown(
        """
        <div class="claim-card">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="claim-number">AI CLAIM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="claim-text">{claim}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="margin-top:1rem;">'
        f'<span class="{badge_class}">{badge_text}</span>'
        f'</div>',
        unsafe_allow_html=True
    )

    reason = confidence.get(
        "reason",
        "There is not enough evidence to determine reliability."
    )

    st.markdown(
        f"""
        <div class="reason-box">
            <b>Why this rating?</b><br>
            {reason}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="evidence-title">Supporting Evidence</div>',
        unsafe_allow_html=True
    )

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
                    "No source description available."
                )

                url = source.get(
                    "url",
                    ""
                )

                st.markdown(
                    f"""
                    <div class="source-card">

                        <div class="source-title">
                            {title}
                        </div>

                        <div class="source-content">
                            {content}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if url:

                    st.link_button(
                        "↗ Open source",
                        url
                    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
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

    speculative = sum(
        1
        for item in analyzed_claims
        if item["confidence"].get("confidence")
        in ["SPECULATIVE", "PURE GENERATION", "LOW"]
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
            "Needs review",
            speculative
        )


# ============================================================
# FOLLOW-UP PROMPT
# ============================================================

def display_question_prompt():

    st.markdown(
        """
        <div class="followup-title">
            ✦ Keep exploring
        </div>

        <div class="followup-text">
            Ask something related to your previous question,
            or explore a completely different topic.
        </div>
        """,
        unsafe_allow_html=True
    )
