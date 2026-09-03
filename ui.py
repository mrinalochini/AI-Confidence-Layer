import streamlit as st


# ============================================================
# THEME
# ============================================================

def load_css():

    st.html("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800'
'&family=Space+Grotesk:wght@400;500;600;700&display=swap'
);

/* =========================
   PAGE
   ========================= */

.stApp {

    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(79, 125, 255, 0.13),
            transparent 24%
        ),
        radial-gradient(
            circle at 95% 10%,
            rgba(255, 119, 105, 0.12),
            transparent 23%
        ),
        radial-gradient(
            circle at 20% 95%,
            rgba(65, 211, 157, 0.10),
            transparent 25%
        ),
        #F7F8FC;

    color: #172033;
}


/* =========================
   LAYOUT
   ========================= */

.block-container {

    max-width: 920px;

    padding-top: 2.2rem;

    padding-bottom: 5rem;
}


/* =========================
   FONTS
   ========================= */

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
        -0.04em;
}


/* =========================
   STREAMLIT CLEANUP
   ========================= */

#MainMenu {

    visibility: hidden;
}

footer {

    visibility: hidden;
}

header {

    background: transparent !important;
}


/* =========================
   INPUT
   ========================= */

.stTextInput > div > div > input {

    background: #FFFFFF !important;

    color: #172033 !important;

    border:
        2px solid #DCE2EE !important;

    border-radius:
        18px !important;

    min-height:
        54px !important;

    padding:
        0.9rem 1.1rem !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-size:
        1rem !important;

    box-shadow:
        0 8px 25px rgba(35,55,90,0.06);
}


.stTextInput > div > div > input:focus {

    border-color:
        #4777E8 !important;

    box-shadow:
        0 0 0 4px rgba(71,119,232,0.10),
        0 10px 30px rgba(35,55,90,0.08);
}


.stTextInput > div > div > input::placeholder {

    color:
        #98A2B3 !important;
}


/* =========================
   MAIN BUTTON
   ========================= */

.stFormSubmitButton > button {

    width: 100%;

    min-height: 52px;

    border: none !important;

    border-radius: 15px !important;

    background:
        linear-gradient(
            100deg,
            #3159D8,
            #4779EE
        ) !important;

    color: white !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-weight: 800 !important;

    box-shadow:
        0 10px 25px rgba(49,89,216,0.22);
}


.stFormSubmitButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 14px 30px rgba(49,89,216,0.28);
}


/* =========================
   NORMAL BUTTONS
   ========================= */

.stButton > button {

    border:
        1px solid #DCE2EE !important;

    background:
        #FFFFFF !important;

    color:
        #344054 !important;

    border-radius:
        13px !important;

    font-family:
        'DM Sans',
        sans-serif !important;

    font-weight:
        700 !important;

    transition:
        all .18s ease;
}


.stButton > button:hover {

    background:
        #F1F5FF !important;

    border-color:
        #9DB5F3 !important;

    color:
        #3159D8 !important;

    transform:
        translateY(-1px);
}


/* =========================
   EXPANDERS
   ========================= */

.stExpander {

    background:
        #FFFFFF !important;

    border:
        1px solid #E1E6EF !important;

    border-radius:
        15px !important;
}


/* =========================
   DIVIDER
   ========================= */

hr {

    border: none !important;

    height: 2px !important;

    background:
        linear-gradient(
            90deg,
            #4777E8,
            #61DDA9,
            #FFB45C,
            #FF7777
        ) !important;

    opacity: .20;
}


/* =========================
   METRICS
   ========================= */

[data-testid="stMetric"] {

    background:
        #FFFFFF;

    border:
        1px solid #E2E7EF;

    border-radius:
        17px;

    padding:
        1rem;

    box-shadow:
        0 7px 20px rgba(35,55,90,0.045);
}


[data-testid="stMetricValue"] {

    font-family:
        'Space Grotesk',
        sans-serif !important;

    color:
        #172033 !important;
}


[data-testid="stMetricLabel"] {

    color:
        #7A8496 !important;
}


/* =========================
   ALERTS
   ========================= */

.stSuccess {

    border-radius:
        13px !important;

    background:
        #EAF9F1 !important;

    border:
        1px solid #B8E9D0 !important;
}


.stWarning {

    border-radius:
        13px !important;

    background:
        #FFF7E8 !important;

    border:
        1px solid #F4D29B !important;
}


.stError {

    border-radius:
        13px !important;

    background:
        #FFF0F1 !important;

    border:
        1px solid #F1C1C6 !important;
}


.stInfo {

    border-radius:
        13px !important;

    background:
        #EDF4FF !important;

    border:
        1px solid #C7D8FB !important;
}

</style>
""")


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown(
        """
        <div style="
            text-align:center;
            padding: 18px 0 12px 0;
        ">

            <div style="
                display:inline-block;
                padding:7px 14px;
                border-radius:30px;
                background:#EAF4FF;
                color:#3159D8;
                font-family:'DM Sans',sans-serif;
                font-size:0.82rem;
                font-weight:700;
                margin-bottom:14px;
            ">
                ✦ AI TRUST & EVIDENCE
            </div>

            <h1 style="
                font-family:'Space Grotesk',sans-serif;
                font-size:3.1rem;
                line-height:1.05;
                margin:0;
                color:#172033;
                letter-spacing:-0.06em;
            ">
                AI Confidence Layer
            </h1>

            <p style="
                font-family:'DM Sans',sans-serif;
                font-size:1.05rem;
                color:#667085;
                margin-top:14px;
            ">
                Don't just get an AI answer.
                <strong style="color:#3159D8;">
                    Understand why you should trust it.
                </strong>
            </p>

        </div>
        """,
    )

    st.divider()


# ============================================================
# FIRST QUESTION
# ============================================================

def display_first_question():

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:28px 10px 12px 10px;
        ">

            <div style="
                font-size:2.2rem;
                margin-bottom:8px;
            ">
                👋
            </div>

            <h2 style="
                font-family:'Space Grotesk',sans-serif;
                color:#172033;
                margin:0;
            ">
                What are you curious about?
            </h2>

            <p style="
                font-family:'DM Sans',sans-serif;
                color:#667085;
                max-width:620px;
                margin:10px auto;
            ">
                Ask naturally. We'll break the answer into claims,
                check the evidence, and help you understand
                what deserves your trust.
            </p>

        </div>
        """,
    )


# ============================================================
# QUICK START
# ============================================================

def display_quick_questions():

    st.markdown(
        """
        <div style="
            margin:20px 0 12px 0;
            font-family:'Space Grotesk',sans-serif;
            font-size:1.25rem;
            font-weight:700;
            color:#172033;
        ">
            ✦ Try it out
        </div>
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "🔬  Test a science claim",
            key="quick_science",
            use_container_width=True
        )

        st.button(
            "🌍  Explore history",
            key="quick_history",
            use_container_width=True
        )

    with col2:

        st.button(
            "🤖  Challenge an AI claim",
            key="quick_ai",
            use_container_width=True
        )

        st.button(
            "💭  Ask something unexpected",
            key="quick_unexpected",
            use_container_width=True
        )


# ============================================================
# QUESTION CARD
# ============================================================

def display_question(question):

    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E7EF;
            border-left:5px solid #4777E8;
            border-radius:18px;
            padding:18px 20px;
            margin:10px 0 22px 0;
            box-shadow:0 8px 25px rgba(35,55,90,0.05);
        ">

            <div style="
                color:#7A8496;
                font-family:'DM Sans',sans-serif;
                font-size:0.78rem;
                font-weight:800;
                letter-spacing:.08em;
                margin-bottom:7px;
            ">
                YOUR QUESTION
            </div>

            <div style="
                color:#172033;
                font-family:'DM Sans',sans-serif;
                font-size:1.05rem;
                font-weight:600;
            ">
                {question}
            </div>

        </div>
        """
    )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown(
        """
        <div style="
            margin:24px 0 14px 0;
        ">

            <div style="
                display:inline-block;
                color:#3159D8;
                background:#EDF3FF;
                border-radius:30px;
                padding:6px 12px;
                font-family:'DM Sans',sans-serif;
                font-size:.76rem;
                font-weight:800;
            ">
                ✦ EVIDENCE CHECK
            </div>

            <h2 style="
                font-family:'Space Grotesk',sans-serif;
                color:#172033;
                margin:10px 0 3px 0;
            ">
                Claim-by-claim analysis
            </h2>

            <p style="
                font-family:'DM Sans',sans-serif;
                color:#667085;
                margin-top:0;
            ">
                Every factual statement is evaluated against
                retrieved evidence.
            </p>

        </div>
        """
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
    # COLORS
    # --------------------------------------------------------

    if level == "HIGH":

        accent = "#35B879"
        background = "#F0FBF5"
        badge = "#DDF7E9"
        label = "✓ HIGH CONFIDENCE"
        description = "Strongly supported"

    elif level == "MEDIUM":

        accent = "#F2A93B"
        background = "#FFF9EE"
        badge = "#FFF0CF"
        label = "◐ MEDIUM CONFIDENCE"
        description = "Partially supported"

    elif level in [
        "SPECULATIVE",
        "PURE GENERATION"
    ]:

        accent = "#E98A35"
        background = "#FFF5EA"
        badge = "#FFE6C8"
        label = "◌ SPECULATIVE"
        description = "Limited external evidence"

    else:

        accent = "#E96B72"
        background = "#FFF2F3"
        badge = "#FFDDE0"
        label = "× LOW CONFIDENCE"
        description = "Needs verification"


    # --------------------------------------------------------
    # CLAIM CARD
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E7EF;
            border-top:4px solid {accent};
            border-radius:20px;
            padding:21px;
            margin:16px 0 8px 0;
            box-shadow:0 10px 30px rgba(35,55,90,0.055);
        ">

            <div style="
                color:#8A94A6;
                font-family:'DM Sans',sans-serif;
                font-size:.72rem;
                font-weight:800;
                letter-spacing:.09em;
                margin-bottom:9px;
            ">
                AI CLAIM
            </div>

            <div style="
                color:#172033;
                font-family:'DM Sans',sans-serif;
                font-size:1.04rem;
                line-height:1.65;
                font-weight:600;
                margin-bottom:16px;
            ">
                {claim}
            </div>

            <div style="
                display:inline-block;
                background:{badge};
                color:{accent};
                border-radius:30px;
                padding:7px 12px;
                font-family:'DM Sans',sans-serif;
                font-size:.78rem;
                font-weight:800;
            ">
                {label}
            </div>

            <span style="
                color:#667085;
                font-family:'DM Sans',sans-serif;
                font-size:.82rem;
                margin-left:7px;
            ">
                {description}
            </span>

        </div>
        """
    )


    # --------------------------------------------------------
    # WHY
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            background:{background};
            border-left:4px solid {accent};
            border-radius:12px;
            padding:14px 16px;
            margin:8px 0 12px 0;
        ">

            <div style="
                color:{accent};
                font-family:'DM Sans',sans-serif;
                font-size:.75rem;
                font-weight:800;
                letter-spacing:.05em;
                margin-bottom:5px;
            ">
                WHY THIS RATING?
            </div>

            <div style="
                color:#475467;
                font-family:'DM Sans',sans-serif;
                font-size:.92rem;
                line-height:1.55;
            ">
                {reason}
            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # EVIDENCE
    # --------------------------------------------------------

    if evidence:

        st.markdown(
            f"""
            <div style="
                display:flex;
                align-items:center;
                gap:8px;
                margin:14px 0 6px 0;
            ">

                <span style="
                    color:#2679C9;
                    background:#EAF5FF;
                    padding:6px 10px;
                    border-radius:20px;
                    font-size:.76rem;
                    font-weight:800;
                    font-family:'DM Sans',sans-serif;
                ">
                    🔎 {len(evidence)} SOURCE
                    {"S" if len(evidence) != 1 else ""}
                </span>

                <span style="
                    color:#7A8496;
                    font-size:.82rem;
                    font-family:'DM Sans',sans-serif;
                ">
                    Supporting evidence
                </span>

            </div>
            """
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
                    f"""
                    <div style="
                        background:#F8FBFF;
                        border:1px solid #DCEAF7;
                        border-radius:14px;
                        padding:15px;
                        margin:8px 0;
                    ">

                        <div style="
                            color:#1F4F76;
                            font-family:'DM Sans',sans-serif;
                            font-weight:700;
                            margin-bottom:7px;
                        ">
                            {title}
                        </div>

                        <div style="
                            color:#667085;
                            font-family:'DM Sans',sans-serif;
                            font-size:.88rem;
                            line-height:1.55;
                        ">
                            {content}
                        </div>

                    </div>
                    """
                )


                if url:

                    st.link_button(
                        "↗  Open source",
                        url
                    )

    else:

        st.markdown(
            """
            <div style="
                background:#FFF5EA;
                border:1px dashed #E8A05B;
                border-radius:14px;
                padding:16px;
                margin-top:10px;
            ">

                <div style="
                    color:#B66A1D;
                    font-family:'DM Sans',sans-serif;
                    font-weight:800;
                    margin-bottom:5px;
                ">
                    ◌ PURE GENERATION / SPECULATIVE
                </div>

                <div style="
                    color:#875A36;
                    font-family:'DM Sans',sans-serif;
                    font-size:.88rem;
                    line-height:1.55;
                ">
                    No supporting external evidence was found.
                    Treat this statement as something to verify
                    rather than established fact.
                </div>

            </div>
            """
        )


    st.markdown("<br>", unsafe_allow_html=True)


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


    review = sum(
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
        """
        <h2 style="
            font-family:'Space Grotesk',sans-serif;
            color:#172033;
            margin:25px 0 15px 0;
        ">
            ✦ Confidence overview
        </h2>
        """
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Claims",
            total
        )


    with col2:

        st.markdown(
            """
            <div style="
                background:#F0FBF5;
                border:1px solid #C6EED8;
                border-radius:17px;
                padding:12px 14px;
                text-align:center;
            ">
                <div style="
                    color:#35B879;
                    font-size:.75rem;
                    font-weight:800;
                ">
                    ✓ STRONG
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            "",
            high,
            label_visibility="collapsed"
        )


    with col3:

        st.markdown(
            """
            <div style="
                background:#FFF9EE;
                border:1px solid #F4DDAF;
                border-radius:17px;
                padding:12px 14px;
                text-align:center;
            ">
                <div style="
                    color:#C98522;
                    font-size:.75rem;
                    font-weight:800;
                ">
                    ◐ PARTIAL
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            "",
            medium,
            label_visibility="collapsed"
        )


    with col4:

        st.markdown(
            """
            <div style="
                background:#FFF2F3;
                border:1px solid #F3C7CB;
                border-radius:17px;
                padding:12px 14px;
                text-align:center;
            ">
                <div style="
                    color:#D75B63;
                    font-size:.75rem;
                    font-weight:800;
                ">
                    ⚠ REVIEW
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            "",
            review,
            label_visibility="collapsed"
        )


# ============================================================
# HOW IT WORKS
# ============================================================

def display_how_it_works():

    with st.expander(
        "◎  How does AI Confidence Layer work?"
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

            You see both the confidence level and why
            that rating was given.
            """
        )


# ============================================================
# FOLLOW-UP
# ============================================================

def display_question_prompt():

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:25px 10px 10px 10px;
        ">

            <div style="
                font-size:1.8rem;
                margin-bottom:5px;
            ">
                ✨
            </div>

            <h2 style="
                font-family:'Space Grotesk',sans-serif;
                color:#172033;
                margin:0;
            ">
                Keep exploring
            </h2>

            <p style="
                font-family:'DM Sans',sans-serif;
                color:#667085;
            ">
                Ask a follow-up, challenge the answer,
                or explore something completely different.
            </p>

        </div>
        """
    )


# ============================================================
# CLEAR
# ============================================================

def display_clear_button():

    if st.button(
        "↺  Start a new conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()
