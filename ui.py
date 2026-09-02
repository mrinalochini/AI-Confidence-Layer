import streamlit as st
import html


# =========================================================
# GLOBAL DESIGN
# =========================================================

def load_css():

    st.markdown(
        """
        <style>

        /* =================================================
           MAIN PAGE
        ================================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(190, 170, 255, 0.35),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 15%,
                    rgba(140, 210, 255, 0.30),
                    transparent 30%
                ),
                linear-gradient(
                    135deg,
                    #f9f7ff 0%,
                    #f5f9ff 50%,
                    #fff8fc 100%
                );

            color: #172033;
        }


        /* =================================================
           PAGE WIDTH
        ================================================= */

        .main .block-container {

            max-width: 1150px;

            padding-top: 3rem;
            padding-bottom: 5rem;

        }


        /* =================================================
           GENERAL FONT
        ================================================= */

        html,
        body,
        [class*="css"] {

            font-family:
                "Trebuchet MS",
                "Segoe UI",
                Arial,
                sans-serif;

        }


        /* =================================================
           HERO SECTION
        ================================================= */

        .hero {

            position: relative;

            overflow: hidden;

            background:
                linear-gradient(
                    135deg,
                    rgba(255,255,255,0.96),
                    rgba(246,242,255,0.97),
                    rgba(239,248,255,0.97)
                );

            border: 1px solid rgba(135, 120, 210, 0.18);

            border-radius: 30px;

            padding: 48px 45px;

            margin-bottom: 38px;

            text-align: center;

            box-shadow:
                0 20px 50px rgba(70, 60, 130, 0.10);

        }


        .hero::before {

            content: "";

            position: absolute;

            width: 180px;
            height: 180px;

            background: rgba(157, 125, 255, 0.13);

            border-radius: 50%;

            top: -80px;
            left: -60px;

        }


        .hero::after {

            content: "";

            position: absolute;

            width: 160px;
            height: 160px;

            background: rgba(75, 190, 255, 0.12);

            border-radius: 50%;

            bottom: -70px;
            right: -50px;

        }


        /* =================================================
           HERO ICON
        ================================================= */

        .hero-icon {

            font-size: 54px;

            margin-bottom: 12px;

        }


        /* =================================================
           HERO TITLE
        ================================================= */

        .hero-title {

            font-family:
                Georgia,
                "Times New Roman",
                serif;

            font-size: 44px;

            font-weight: 800;

            letter-spacing: -1px;

            background:
                linear-gradient(
                    90deg,
                    #7048e8,
                    #a23fc7,
                    #3c82e8
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            margin-bottom: 14px;

        }


        /* =================================================
           HERO SUBTITLE
        ================================================= */

        .hero-subtitle {

            font-family:
                "Trebuchet MS",
                sans-serif;

            font-size: 18px;

            line-height: 1.7;

            color: #657086;

            max-width: 700px;

            margin: auto;

        }


        .hero-highlight {

            color: #7048e8;

            font-weight: 750;

        }


        /* =================================================
           QUESTION LABEL
        ================================================= */

        .question-label {

            font-family:
                Georgia,
                serif;

            font-size: 21px;

            font-weight: 700;

            color: #252c42;

            margin-bottom: 7px;

        }


        /* =================================================
           TEXT INPUT
        ================================================= */

        div[data-testid="stTextInput"] {

            margin-bottom: 12px;

        }


        div[data-baseweb="input"] {

            background: #ffffff !important;

            border: 2px solid #e2e4ee !important;

            border-radius: 16px !important;

            min-height: 55px !important;

            box-shadow:
                0 5px 18px rgba(60, 70, 120, 0.06);

            transition: all 0.2s ease;

        }


        div[data-baseweb="input"]:hover {

            border-color: #b7a6f5 !important;

        }


        div[data-baseweb="input"]:focus-within {

            border-color: #8064e8 !important;

            box-shadow:
                0 0 0 4px rgba(128, 100, 232, 0.12),
                0 7px 20px rgba(80, 60, 150, 0.08) !important;

        }


        /* IMPORTANT:
           Make the typed question clearly visible
        */

        div[data-baseweb="input"] input {

            color: #172033 !important;

            background: #ffffff !important;

            font-family:
                "Trebuchet MS",
                "Segoe UI",
                sans-serif !important;

            font-size: 17px !important;

            font-weight: 600 !important;

        }


        div[data-baseweb="input"] input::placeholder {

            color: #98a0b3 !important;

            opacity: 1 !important;

            font-weight: 400 !important;

        }


        /* =================================================
           ANALYZE BUTTON
        ================================================= */

        .stButton > button {

            background:
                linear-gradient(
                    135deg,
                    #7655e8,
                    #a04de0,
                    #4d8de8
                ) !important;

            color: white !important;

            border: none !important;

            border-radius: 14px !important;

            padding: 13px 28px !important;

            font-family:
                "Trebuchet MS",
                sans-serif !important;

            font-size: 16px !important;

            font-weight: 750 !important;

            letter-spacing: 0.2px;

            box-shadow:
                0 8px 20px rgba(110, 75, 210, 0.25);

            transition: all 0.2s ease;

        }


        .stButton > button:hover {

            transform: translateY(-2px);

            box-shadow:
                0 12px 26px rgba(110, 75, 210, 0.32);

        }


        /* =================================================
           SECTION TITLE
        ================================================= */

        .section-title {

            font-family:
                Georgia,
                "Times New Roman",
                serif;

            font-size: 29px;

            font-weight: 800;

            color: #252c42;

            margin-top: 42px;

            margin-bottom: 8px;

        }


        .section-description {

            font-family:
                "Segoe UI",
                sans-serif;

            font-size: 15px;

            line-height: 1.6;

            color: #7a8294;

            margin-bottom: 25px;

        }


        /* =================================================
           CLAIM CARD
        ================================================= */

        .claim-card {

            background: rgba(255,255,255,0.97);

            border: 1px solid #e7e8f0;

            border-radius: 20px;

            padding: 28px;

            margin-bottom: 18px;

            box-shadow:
                0 8px 25px rgba(50, 55, 90, 0.07);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;

        }


        .claim-card:hover {

            transform: translateY(-2px);

            box-shadow:
                0 12px 30px rgba(50, 55, 90, 0.10);

        }


        /* =================================================
           CLAIM HEADER
        ================================================= */

        .claim-header {

            display: flex;

            justify-content: space-between;

            align-items: center;

            margin-bottom: 17px;

        }


        .claim-label {

            font-family:
                "Courier New",
                monospace;

            font-size: 12px;

            font-weight: 700;

            letter-spacing: 1.4px;

            text-transform: uppercase;

            color: #9299aa;

        }


        /* =================================================
           CONFIDENCE BADGES
        ================================================= */

        .confidence-badge {

            padding: 8px 14px;

            border-radius: 999px;

            font-family:
                "Trebuchet MS",
                sans-serif;

            font-size: 12px;

            font-weight: 800;

            letter-spacing: 0.4px;

        }


        .confidence-high {

            background:
                linear-gradient(
                    135deg,
                    #e4f9ec,
                    #d7f5e5
                );

            color: #16834c;

        }


        .confidence-medium {

            background:
                linear-gradient(
                    135deg,
                    #fff5d9,
                    #fff0c5
                );

            color: #a86d00;

        }


        .confidence-low {

            background:
                linear-gradient(
                    135deg,
                    #ffe9ec,
                    #ffdddd
                );

            color: #c33c50;

        }


        /* =================================================
           CLAIM TEXT
        ================================================= */

        .claim-text {

            font-family:
                Georgia,
                "Times New Roman",
                serif;

            font-size: 21px;

            line-height: 1.65;

            font-weight: 600;

            color: #20283b;

            margin-bottom: 21px;

        }


        /* =================================================
           WHY BOX
        ================================================= */

        .reason-box {

            background:
                linear-gradient(
                    135deg,
                    #f8f5ff,
                    #f3f8ff
                );

            border-left: 4px solid #8262e8;

            border-radius: 12px;

            padding: 16px 19px;

            margin-bottom: 5px;

        }


        .reason-title {

            font-family:
                "Trebuchet MS",
                sans-serif;

            font-size: 13px;

            font-weight: 800;

            color: #7555d9;

            margin-bottom: 6px;

        }


        .reason-text {

            font-family:
                "Segoe UI",
                sans-serif;

            font-size: 15px;

            line-height: 1.55;

            color: #60697b;

        }


        /* =================================================
           EVIDENCE EXPANDER
        ================================================= */

        div[data-testid="stExpander"] {

            background: rgba(255,255,255,0.95) !important;

            border: 1px solid #e4e6ef !important;

            border-radius: 14px !important;

            margin-top: 8px;

        }


        div[data-testid="stExpander"] summary {

            font-family:
                "Trebuchet MS",
                sans-serif !important;

            font-weight: 700 !important;

            color: #424a60 !important;

        }


        /* =================================================
           EVIDENCE SOURCE
        ================================================= */

        .source-card {

            background: #fafbff;

            border: 1px solid #e9ebf3;

            border-radius: 12px;

            padding: 16px;

            margin-top: 10px;

        }


        .source-name {

            font-family:
                Georgia,
                serif;

            font-size: 15px;

            font-weight: 700;

            color: #30394e;

            margin-bottom: 7px;

        }


        .source-content {

            font-family:
                "Segoe UI",
                sans-serif;

            font-size: 13px;

            line-height: 1.55;

            color: #687185;

        }


        .source-link {

            display: inline-block;

            margin-top: 9px;

            font-family:
                "Trebuchet MS",
                sans-serif;

            font-size: 13px;

            color: #7054df;

            text-decoration: none;

            font-weight: 750;

        }


        /* =================================================
           SUMMARY
        ================================================= */

        .summary-grid {

            display: flex;

            gap: 16px;

            margin-bottom: 30px;

        }


        .summary-card {

            flex: 1;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #fafaff
                );

            border: 1px solid #e5e7ef;

            border-radius: 17px;

            padding: 21px;

            text-align: center;

            box-shadow:
                0 6px 18px rgba(50, 55, 90, 0.05);

        }


        .summary-number {

            font-family:
                Georgia,
                serif;

            font-size: 30px;

            font-weight: 800;

            background:
                linear-gradient(
                    90deg,
                    #7250dc,
                    #4788e8
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

        }


        .summary-label {

            font-family:
                "Trebuchet MS",
                sans-serif;

            font-size: 13px;

            color: #7b8497;

            margin-top: 4px;

        }


        /* =================================================
           STREAMLIT ALERTS
        ================================================= */

        div[data-testid="stAlert"] {

            border-radius: 13px;

        }


        /* =================================================
           MOBILE
        ================================================= */

        @media (max-width: 700px) {

            .hero {

                padding: 35px 20px;

            }

            .hero-title {

                font-size: 34px;

            }

            .hero-subtitle {

                font-size: 16px;

            }

            .summary-grid {

                flex-direction: column;

            }

            .claim-header {

                align-items: flex-start;

                gap: 10px;

                flex-direction: column;

            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HERO
# =========================================================

def display_header():

    st.html(
        """
        <div class="hero">

            <div class="hero-icon">
                🧠✨
            </div>

            <div class="hero-title">
                AI Confidence Layer
            </div>

            <div class="hero-subtitle">

                Get answers from AI —
                then discover
                <span class="hero-highlight">
                    how much you can trust them.
                </span>

                <br>

                We check individual claims against
                supporting evidence so you can make
                better-informed decisions.

            </div>

        </div>
        """
    )


# =========================================================
# ANALYSIS HEADER
# =========================================================

def display_analysis_header():

    st.html(
        """
        <div class="section-title">
            🔍 Claim-by-Claim Analysis
        </div>

        <div class="section-description">

            We've broken the AI response into individual
            claims and checked the evidence behind each one.

        </div>
        """
    )


# =========================================================
# CLAIM DISPLAY
# =========================================================

def display_claim(claim, confidence, evidence):

    level = confidence["confidence"]

    if level == "HIGH":

        icon = "🟢"
        badge_class = "confidence-high"

    elif level == "MEDIUM":

        icon = "🟡"
        badge_class = "confidence-medium"

    else:

        icon = "🔴"
        badge_class = "confidence-low"


    safe_claim = html.escape(str(claim))

    safe_reason = html.escape(
        str(
            confidence.get(
                "reason",
                "No explanation was provided."
            )
        )
    )


    # -----------------------------------------------------
    # CLAIM CARD
    # -----------------------------------------------------

    st.html(
        f"""
        <div class="claim-card">

            <div class="claim-header">

                <div class="claim-label">
                    AI CLAIM
                </div>

                <div class="confidence-badge {badge_class}">
                    {icon} {html.escape(level)} CONFIDENCE
                </div>

            </div>


            <div class="claim-text">
                {safe_claim}
            </div>


            <div class="reason-box">

                <div class="reason-title">
                    💡 Why this confidence level?
                </div>

                <div class="reason-text">
                    {safe_reason}
                </div>

            </div>

        </div>
        """
    )


    # -----------------------------------------------------
    # EVIDENCE
    # -----------------------------------------------------

    with st.expander("📚  View supporting evidence"):

        if not evidence:

            st.info(
                "We couldn't find supporting evidence for this claim."
            )

        else:

            for source in evidence:

                title = html.escape(
                    str(
                        source.get(
                            "title",
                            "Unknown source"
                        )
                    )
                )

                content = html.escape(
                    str(
                        source.get(
                            "content",
                            ""
                        )
                    )
                )

                url = str(
                    source.get(
                        "url",
                        "#"
                    )
                )


                st.html(
                    f"""
                    <div class="source-card">

                        <div class="source-name">
                            📖 {title}
                        </div>

                        <div class="source-content">
                            {content}
                        </div>

                        <a
                            class="source-link"
                            href="{url}"
                            target="_blank"
                        >
                            Read source →
                        </a>

                    </div>
                    """
                )


# =========================================================
# SUMMARY
# =========================================================

def display_summary(analyzed_claims):

    total = len(analyzed_claims)

    high = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"] == "HIGH"
    )

    medium = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"] == "MEDIUM"
    )

    low = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"] == "LOW"
    )


    st.html(
        f"""
        <div class="section-title">
            ✨ Trust Summary
        </div>

        <div class="summary-grid">


            <div class="summary-card">

                <div class="summary-number">
                    {total}
                </div>

                <div class="summary-label">
                    Claims Analyzed
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-number">
                    {high}
                </div>

                <div class="summary-label">
                    🟢 High Confidence
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-number">
                    {medium}
                </div>

                <div class="summary-label">
                    🟡 Medium Confidence
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-number">
                    {low}
                </div>

                <div class="summary-label">
                    🔴 Low Confidence
                </div>

            </div>


        </div>
        """
    )
