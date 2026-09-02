import streamlit as st
import html


# =========================================================
# GLOBAL CSS
# =========================================================

def load_css():

    st.markdown(
        """
        <style>

        /* =========================
           PAGE
        ========================= */

        .stApp {
            background: #f6f7fb;
            color: #172033;
        }

        .main .block-container {
            max-width: 1100px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }


        /* =========================
           GLOBAL FONT
        ========================= */

        html, body, [class*="css"] {
            font-family: "Segoe UI", "Trebuchet MS", Arial, sans-serif;
        }

        p, span, div, label {
            font-family: "Segoe UI", "Trebuchet MS", Arial, sans-serif;
        }


        /* =========================
           HERO
        ========================= */

        .hero {
            background: linear-gradient(
                135deg,
                #ffffff 0%,
                #f4f1ff 50%,
                #eef4ff 100%
            );

            border: 1px solid #e5e7f0;
            border-radius: 24px;

            padding: 42px 40px;

            margin-bottom: 35px;

            text-align: center;

            box-shadow:
                0 10px 30px rgba(40, 50, 90, 0.08);
        }

        .hero-icon {
            font-size: 48px;
            margin-bottom: 10px;
        }

        .hero-title {
            font-size: 38px;
            font-weight: 750;
            letter-spacing: -1px;
            color: #172033;
            margin-bottom: 12px;
        }

        .hero-subtitle {
            font-size: 17px;
            line-height: 1.6;
            color: #667085;
            max-width: 650px;
            margin: auto;
        }

        .hero-highlight {
            color: #6d4aff;
            font-weight: 700;
        }


        /* =========================
           QUESTION AREA
        ========================= */

        .question-label {
            font-size: 18px;
            font-weight: 650;
            color: #172033;
            margin-bottom: 8px;
        }


        /* =========================
           INPUT
        ========================= */

        div[data-baseweb="input"] {
            border-radius: 12px !important;
            border: 1px solid #dfe3ed !important;
            background: white !important;
        }

        div[data-baseweb="input"]:focus-within {
            border: 1px solid #8066ff !important;
            box-shadow: 0 0 0 3px rgba(128, 102, 255, 0.12) !important;
        }

        input {
            font-size: 16px !important;
            color: #172033 !important;
        }


        /* =========================
           BUTTON
        ========================= */

        .stButton > button {
            border: none;
            border-radius: 12px;

            background: linear-gradient(
                135deg,
                #7456f5,
                #5b8def
            );

            color: white;

            font-size: 16px;
            font-weight: 650;

            padding: 12px 25px;

            box-shadow:
                0 6px 15px rgba(100, 85, 220, 0.25);

            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);

            box-shadow:
                0 9px 20px rgba(100, 85, 220, 0.30);
        }


        /* =========================
           SECTION TITLE
        ========================= */

        .section-title {
            font-size: 25px;
            font-weight: 750;

            color: #172033;

            margin-top: 40px;
            margin-bottom: 22px;
        }

        .section-description {
            color: #667085;
            font-size: 15px;
            margin-top: -14px;
            margin-bottom: 25px;
        }


        /* =========================
           CLAIM CARD
        ========================= */

        .claim-card {
            background: white;

            border: 1px solid #e4e7ef;

            border-radius: 18px;

            padding: 26px;

            margin-bottom: 20px;

            box-shadow:
                0 5px 18px rgba(30, 40, 70, 0.06);
        }

        .claim-header {
            display: flex;
            justify-content: space-between;
            align-items: center;

            margin-bottom: 18px;
        }

        .claim-label {
            font-size: 13px;
            font-weight: 700;

            text-transform: uppercase;
            letter-spacing: 1px;

            color: #7b8498;
        }


        /* =========================
           CONFIDENCE BADGES
        ========================= */

        .confidence-badge {
            padding: 7px 13px;

            border-radius: 999px;

            font-size: 12px;
            font-weight: 750;

            letter-spacing: 0.5px;
        }

        .confidence-high {
            background: #e8f8ee;
            color: #16834a;
        }

        .confidence-medium {
            background: #fff5d9;
            color: #a66b00;
        }

        .confidence-low {
            background: #ffe9e9;
            color: #c43d3d;
        }


        /* =========================
           CLAIM TEXT
        ========================= */

        .claim-text {
            font-size: 19px;

            line-height: 1.65;

            font-weight: 550;

            color: #20283a;

            margin-bottom: 20px;
        }


        /* =========================
           WHY BOX
        ========================= */

        .reason-box {
            background: #f7f8fc;

            border-left: 4px solid #7456f5;

            border-radius: 10px;

            padding: 15px 18px;

            margin-bottom: 18px;
        }

        .reason-title {
            font-size: 13px;
            font-weight: 750;

            color: #7456f5;

            margin-bottom: 5px;
        }

        .reason-text {
            font-size: 15px;
            line-height: 1.5;

            color: #596273;
        }


        /* =========================
           EVIDENCE
        ========================= */

        .evidence-title {
            font-size: 14px;

            font-weight: 700;

            color: #30394d;

            margin-bottom: 8px;
        }

        .source-card {
            background: #fafbfe;

            border: 1px solid #e8eaf1;

            border-radius: 10px;

            padding: 14px 16px;

            margin-top: 10px;
        }

        .source-name {
            font-size: 14px;
            font-weight: 700;

            color: #344054;

            margin-bottom: 5px;
        }

        .source-content {
            font-size: 13px;

            line-height: 1.5;

            color: #667085;
        }

        .source-link {
            display: inline-block;

            margin-top: 8px;

            font-size: 13px;

            color: #635bff;

            text-decoration: none;

            font-weight: 650;
        }


        /* =========================
           SUMMARY
        ========================= */

        .summary-grid {
            display: flex;
            gap: 15px;

            margin-bottom: 30px;
        }

        .summary-card {
            flex: 1;

            background: white;

            border: 1px solid #e4e7ef;

            border-radius: 15px;

            padding: 20px;

            text-align: center;

            box-shadow:
                0 4px 15px rgba(30, 40, 70, 0.05);
        }

        .summary-number {
            font-size: 28px;

            font-weight: 750;

            color: #172033;
        }

        .summary-label {
            font-size: 13px;

            color: #7b8498;

            margin-top: 4px;
        }


        /* =========================
           EXPANDER
        ========================= */

        div[data-testid="stExpander"] {
            border: 1px solid #e5e7ef !important;

            border-radius: 12px !important;

            background: #ffffff !important;
        }


        /* =========================
           WARNINGS
        ========================= */

        div[data-testid="stAlert"] {
            border-radius: 12px;
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

            <div class="hero-icon">🧠</div>

            <div class="hero-title">
                AI Confidence Layer
            </div>

            <div class="hero-subtitle">
                Don't just get an AI answer.
                Understand
                <span class="hero-highlight">
                    why you should trust it.
                </span>
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
            🔬 Claim-by-Claim Analysis
        </div>

        <div class="section-description">
            Each claim is evaluated against external evidence
            to help you understand how trustworthy the answer is.
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
        str(confidence.get("reason", "No explanation provided."))
    )


    # Main claim card

    st.html(
        f"""
        <div class="claim-card">

            <div class="claim-header">

                <div class="claim-label">
                    AI Claim
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
                    Why this confidence level?
                </div>

                <div class="reason-text">
                    {safe_reason}
                </div>

            </div>

        </div>
        """
    )


    # Evidence section

    with st.expander("📚 View supporting evidence"):

        if not evidence:

            st.info("No supporting evidence was found.")

        else:

            for source in evidence:

                title = html.escape(
                    str(source.get("title", "Unknown source"))
                )

                content = html.escape(
                    str(source.get("content", ""))
                )

                url = str(
                    source.get("url", "#")
                )

                st.html(
                    f"""
                    <div class="source-card">

                        <div class="source-name">
                            {title}
                        </div>

                        <div class="source-content">
                            {content}
                        </div>

                        <a
                            class="source-link"
                            href="{url}"
                            target="_blank"
                        >
                            Open source →
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
            📊 Trust Summary
        </div>

        <div class="summary-grid">

            <div class="summary-card">

                <div class="summary-number">
                    {total}
                </div>

                <div class="summary-label">
                    Total Claims
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-number">
                    {high}
                </div>

                <div class="summary-label">
                    High Confidence
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-number">
                    {medium}
                </div>

                <div class="summary-label">
                    Medium Confidence
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-number">
                    {low}
                </div>

                <div class="summary-label">
                    Low Confidence
                </div>

            </div>

        </div>
        """
    )
