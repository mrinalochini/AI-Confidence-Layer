import streamlit as st
import html


# =========================================================
# GLOBAL STYLING
# =========================================================

def load_css():

    st.markdown(
        """
        <style>

        /* =====================================================
           IMPORT BEAUTIFUL FONTS
        ===================================================== */

        @import url(
            'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Quicksand:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap'
        );


        /* =====================================================
           PAGE BACKGROUND
        ===================================================== */

        .stApp {

            background:
                radial-gradient(
                    circle at 5% 5%,
                    rgba(215, 190, 255, 0.55),
                    transparent 25%
                ),

                radial-gradient(
                    circle at 95% 5%,
                    rgba(180, 225, 255, 0.55),
                    transparent 25%
                ),

                radial-gradient(
                    circle at 50% 100%,
                    rgba(255, 210, 235, 0.35),
                    transparent 30%
                ),

                linear-gradient(
                    135deg,
                    #f9f7ff,
                    #f3f8ff 50%,
                    #fff7fc
                );

            color: #172033;

        }


        /* =====================================================
           MAIN CONTAINER
        ===================================================== */

        .main .block-container {

            max-width: 1150px;

            padding-top: 3rem;
            padding-bottom: 5rem;

        }


        /* =====================================================
           DEFAULT TEXT
        ===================================================== */

.stApp {
    color: #172033;
}

.stApp p {
    font-family: "Poppins", sans-serif;
}


        /* =====================================================
           HERO
        ===================================================== */

        .hero {

            position: relative;

            overflow: hidden;

            background:
                linear-gradient(
                    135deg,
                    rgba(255,255,255,0.98),
                    rgba(247,242,255,0.97),
                    rgba(239,248,255,0.98)
                );

            border-radius: 32px;

            border: 1px solid rgba(125, 105, 210, 0.15);

            padding: 50px 40px 46px;

            margin-bottom: 40px;

            text-align: center;

            box-shadow:
                0 20px 55px rgba(78, 67, 130, 0.10);

        }


        /* Decorative blobs */

        .hero::before {

            content: "";

            position: absolute;

            width: 190px;
            height: 190px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    rgba(190, 130, 255, 0.20),
                    transparent 70%
                );

            top: -90px;
            left: -60px;

        }


        .hero::after {

            content: "";

            position: absolute;

            width: 180px;
            height: 180px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    rgba(80, 190, 255, 0.18),
                    transparent 70%
                );

            bottom: -90px;
            right: -60px;

        }


        /* =====================================================
           HERO ICON
        ===================================================== */

        .hero-icon {

            font-size: 58px;

            line-height: 1;

            margin-bottom: 18px;

            position: relative;

            z-index: 2;

        }


        /* =====================================================
           HERO TITLE
        ===================================================== */

        .hero-title {

            font-family:
                "Playfair Display",
                Georgia,
                serif;

            font-size: 46px;

            font-weight: 800;

            line-height: 1.15;

            background:
                linear-gradient(
                    90deg,
                    #6845e8,
                    #b34dcc,
                    #3f83e8
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            margin-bottom: 15px;

            position: relative;

            z-index: 2;

        }


        /* =====================================================
           HERO SUBTITLE
        ===================================================== */

        .hero-subtitle {

            font-family:
                "Quicksand",
                sans-serif;

            font-size: 18px;

            font-weight: 500;

            line-height: 1.7;

            color: #68738a;

            max-width: 720px;

            margin: auto;

            position: relative;

            z-index: 2;

        }


        .hero-highlight {

            color: #7650e8;

            font-weight: 700;

        }


        /* =====================================================
           QUESTION LABEL
        ===================================================== */

        div[data-testid="stTextInput"] label {

            color: #343b53 !important;

            font-family:
                "Space Grotesk",
                sans-serif !important;

            font-size: 18px !important;

            font-weight: 700 !important;

            opacity: 1 !important;

        }


        div[data-testid="stTextInput"] label p {

            color: #343b53 !important;

            font-family:
                "Space Grotesk",
                sans-serif !important;

            font-weight: 700 !important;

        }


        /* =====================================================
           INPUT CONTAINER
        ===================================================== */

        div[data-testid="stTextInput"] {

            margin-bottom: 14px;

        }


        div[data-testid="stTextInput"] > div {

            background: transparent !important;

        }


        /* =====================================================
           INPUT BOX — IMPORTANT FIX
        ===================================================== */

        div[data-testid="stTextInput"] div[data-baseweb="input"] {

            background-color: #ffffff !important;

            border: 2px solid #e2e4ef !important;

            border-radius: 17px !important;

            min-height: 58px !important;

            box-shadow:
                0 7px 22px rgba(70, 70, 120, 0.08) !important;

            transition:
                border 0.2s ease,
                box-shadow 0.2s ease,
                transform 0.2s ease !important;

        }


        /* =====================================================
           ACTUAL TEXT INPUT
           This is what fixes the invisible typing.
        ===================================================== */

        div[data-testid="stTextInput"] input {

            background-color: #ffffff !important;

            color: #172033 !important;

            -webkit-text-fill-color: #172033 !important;

            caret-color: #7650e8 !important;

            font-family:
                "Quicksand",
                sans-serif !important;

            font-size: 17px !important;

            font-weight: 600 !important;

            opacity: 1 !important;

        }


        /* Placeholder */

        div[data-testid="stTextInput"] input::placeholder {

            color: #9aa2b4 !important;

            -webkit-text-fill-color: #9aa2b4 !important;

            opacity: 1 !important;

            font-family:
                "Quicksand",
                sans-serif !important;

            font-weight: 500 !important;

        }


        /* =====================================================
           INPUT FOCUS
        ===================================================== */

        div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {

            background-color: #ffffff !important;

            border-color: #8564ef !important;

            box-shadow:
                0 0 0 4px rgba(133, 100, 239, 0.12),
                0 10px 28px rgba(105, 80, 190, 0.12) !important;

            transform: translateY(-1px);

        }


        /* =====================================================
           ANALYZE BUTTON
        ===================================================== */

        .stButton > button {

            background:
                linear-gradient(
                    135deg,
                    #7754e8,
                    #a14ed8,
                    #4d8ee8
                ) !important;

            color: #ffffff !important;

            border: none !important;

            border-radius: 15px !important;

            min-height: 50px !important;

            padding:
                10px 27px !important;

            font-family:
                "Space Grotesk",
                sans-serif !important;

            font-size: 16px !important;

            font-weight: 700 !important;

            letter-spacing: 0.2px;

            box-shadow:
                0 8px 22px rgba(106, 77, 210, 0.25);

            transition: all 0.2s ease !important;

        }


        .stButton > button:hover {

            transform: translateY(-2px) scale(1.01);

            box-shadow:
                0 13px 28px rgba(106, 77, 210, 0.32);

        }


        /* =====================================================
           SECTION TITLE
        ===================================================== */

        .section-title {

            font-family:
                "Playfair Display",
                Georgia,
                serif;

            font-size: 30px;

            font-weight: 800;

            color: #252c42;

            margin-top: 45px;

            margin-bottom: 8px;

        }


        .section-description {

            font-family:
                "Quicksand",
                sans-serif;

            font-size: 15px;

            font-weight: 500;

            line-height: 1.7;

            color: #7a8397;

            margin-bottom: 26px;

        }


        /* =====================================================
           CLAIM CARD
        ===================================================== */

        .claim-card {

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #fcfbff
                );

            border: 1px solid #e5e6ef;

            border-radius: 21px;

            padding: 28px;

            margin-bottom: 19px;

            box-shadow:
                0 9px 27px rgba(45, 50, 90, 0.07);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;

        }


        .claim-card:hover {

            transform: translateY(-3px);

            box-shadow:
                0 14px 35px rgba(45, 50, 90, 0.11);

        }


        /* =====================================================
           CLAIM HEADER
        ===================================================== */

        .claim-header {

            display: flex;

            justify-content: space-between;

            align-items: center;

            margin-bottom: 18px;

        }


        .claim-label {

            font-family:
                "Space Grotesk",
                sans-serif;

            font-size: 12px;

            font-weight: 700;

            letter-spacing: 1.5px;

            color: #9aa1b2;

        }


        /* =====================================================
           CONFIDENCE BADGES
        ===================================================== */

        .confidence-badge {

            padding: 8px 15px;

            border-radius: 999px;

            font-family:
                "Poppins",
                sans-serif;

            font-size: 12px;

            font-weight: 800;

        }


        .confidence-high {

            background:
                linear-gradient(
                    135deg,
                    #ddf8e9,
                    #cff4e0
                );

            color: #137a46;

            box-shadow:
                0 3px 10px rgba(35, 170, 95, 0.10);

        }


        .confidence-medium {

            background:
                linear-gradient(
                    135deg,
                    #fff4d4,
                    #ffedbd
                );

            color: #a26800;

        }


        .confidence-low {

            background:
                linear-gradient(
                    135deg,
                    #ffe6eb,
                    #ffd9df
                );

            color: #c23b50;

        }
/* ==========================================
   PURE GENERATION / SPECULATIVE
========================================== */

.speculative-card {

    background: linear-gradient(
        135deg,
        #FFF9EB,
        #FFF2D5
    );

    border: 1px solid #F6C567;

    border-radius: 22px;

    box-shadow: 0 8px 25px rgba(228,160,45,0.12);

}

.speculative-badge {

    background: #FFF3D4;

    color: #B45309;

    border-radius: 999px;

    padding: 8px 14px;

    font-weight: 700;

}

.speculative-underline {

    text-decoration: underline;

    text-decoration-style: dashed;

    text-decoration-color: #D97706;

    text-decoration-thickness: 3px;

    text-underline-offset: 8px;

}

        /* =====================================================
           CLAIM TEXT
        ===================================================== */

        .claim-text {

            font-family:
                "Playfair Display",
                Georgia,
                serif;

            font-size: 21px;

            line-height: 1.65;

            font-weight: 600;

            color: #20283b;

            margin-bottom: 21px;

        }


        /* =====================================================
           WHY BOX
        ===================================================== */

        .reason-box {

            background:
                linear-gradient(
                    135deg,
                    #f8f3ff,
                    #f1f8ff
                );

            border-left:
                4px solid #815ee8;

            border-radius: 13px;

            padding: 16px 19px;

        }


        .reason-title {

            font-family:
                "Space Grotesk",
                sans-serif;

            font-size: 13px;

            font-weight: 800;

            color: #7351d4;

            margin-bottom: 6px;

        }


        .reason-text {

            font-family:
                "Quicksand",
                sans-serif;

            font-size: 15px;

            font-weight: 500;

            line-height: 1.55;

            color: #626b7e;

        }


        /* =====================================================
   EVIDENCE EXPANDER
   ===================================================== */

div[data-testid="stExpander"] {
    background: #ffffff !important;
    border: 1px solid #e4e6ef !important;
    border-radius: 15px !important;
    margin-top: 10px !important;
    margin-bottom: 12px !important;
    box-shadow: 0 5px 16px rgba(50, 55, 90, 0.05) !important;
}


/* Keep Streamlit's internal expander layout intact */

div[data-testid="stExpander"] summary {
    color: #414960 !important;
    font-family: "Space Grotesk", sans-serif !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}


/* Don't modify Streamlit's internal icons */

div[data-testid="stExpander"] summary svg {
    width: 1.2rem !important;
    height: 1.2rem !important;
}


        /* =====================================================
           SOURCE CARD
        ===================================================== */

        .source-card {

            background:
                linear-gradient(
                    135deg,
                    #fbfaff,
                    #f8fbff
                );

            border:
                1px solid #e7e9f1;

            border-radius: 13px;

            padding: 17px;

            margin-top: 11px;

        }


        .source-name {

            font-family:
                "Playfair Display",
                Georgia,
                serif;

            font-size: 16px;

            font-weight: 700;

            color: #30384e;

            margin-bottom: 7px;

        }


        .source-content {

            font-family:
                "Quicksand",
                sans-serif;

            font-size: 13px;

            font-weight: 500;

            line-height: 1.6;

            color: #687185;

        }


        .source-link {

            display: inline-block;

            margin-top: 10px;

            font-family:
                "Space Grotesk",
                sans-serif;

            font-size: 13px;

            font-weight: 700;

            color: #7152dc;

            text-decoration: none;

        }


        /* =====================================================
           SUMMARY
        ===================================================== */

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
                    #faf9ff
                );

            border:
                1px solid #e4e6ef;

            border-radius: 18px;

            padding: 22px;

            text-align: center;

            box-shadow:
                0 7px 20px rgba(50, 55, 90, 0.05);

        }


        .summary-number {

            font-family:
                "Playfair Display",
                Georgia,
                serif;

            font-size: 31px;

            font-weight: 800;

            background:
                linear-gradient(
                    90deg,
                    #714dd9,
                    #a94bcf,
                    #4b86df
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

        }


        .summary-label {

            font-family:
                "Quicksand",
                sans-serif;

            font-size: 13px;

            font-weight: 600;

            color: #7a8397;

            margin-top: 5px;

        }


        /* =====================================================
           ALERTS
        ===================================================== */

        div[data-testid="stAlert"] {

            border-radius: 13px;

            font-family:
                "Quicksand",
                sans-serif;

        }


        /* =====================================================
           SPINNER
        ===================================================== */

        div[data-testid="stSpinner"] {

            font-family:
                "Quicksand",
                sans-serif !important;

        }


        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 700px) {

            .hero {

                padding:
                    38px 20px;

            }

            .hero-title {

                font-size: 35px;

            }

            .hero-subtitle {

                font-size: 16px;

            }

            .summary-grid {

                flex-direction: column;

            }

            .claim-header {

                flex-direction: column;

                align-items: flex-start;

                gap: 12px;

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

                Don't just get an AI answer.

                Discover
                <span class="hero-highlight">
                    why you can trust it.
                </span>

                <br>

                We break AI responses into claims,
                check the evidence, and help you
                make informed decisions.

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

            Each part of the AI answer is checked against
            supporting evidence so you can see what holds up.

        </div>
        """
    )


# =========================================================
# CLAIM DISPLAY
# =========================================================

import html
import streamlit as st

def display_claim(claim, confidence, evidence):

    level = confidence["confidence"].upper()
    reason = confidence.get("reason", "")

    # ------------------------------
    # Confidence Themes
    # ------------------------------

    if level == "HIGH":
        icon = "🟢"
        badge_color = "#16A34A"
        badge_bg = "#E8FFF0"
        card_bg = "#FFFFFF"
        underline = "none"
        title = "Verified Claim"

    elif level == "MEDIUM":
        icon = "🟡"
        badge_color = "#2563EB"
        badge_bg = "#EAF4FF"
        card_bg = "#FCFEFF"
        underline = "none"
        title = "Likely Supported Claim"

    elif level == "SPECULATIVE":
        icon = "✨"
        badge_color = "#B45309"
        badge_bg = "#FFF4D6"

        # Warm amber gradient
        card_bg = """
        linear-gradient(
            135deg,
            #FFF9EC 0%,
            #FFF2CC 100%
        )
        """

        underline = "3px dashed #D97706"
        title = "AI Generated Insight"

    else:
        icon = "🔴"
        badge_color = "#DC2626"
        badge_bg = "#FFECEC"
        card_bg = "#FFFDFD"
        underline = "none"
        title = "Low Confidence Claim"

    # Escape text
    safe_claim = html.escape(claim)
    safe_reason = html.escape(reason)

    # ------------------------------
    # Claim Card
    # ------------------------------

    st.markdown(
        f"""
        <div style="
            background:{card_bg};
            border-radius:22px;
            padding:24px;
            margin-bottom:20px;
            border:1px solid #EFE7D0;
            box-shadow:0 10px 30px rgba(0,0,0,0.05);
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                margin-bottom:18px;
            ">

                <div style="
                    font-family:'Space Grotesk';
                    font-size:13px;
                    letter-spacing:1.5px;
                    color:#7A7A7A;
                    text-transform:uppercase;
                    font-weight:700;
                ">
                    {title}
                </div>

                <div style="
                    background:{badge_bg};
                    color:{badge_color};
                    padding:8px 14px;
                    border-radius:999px;
                    font-weight:700;
                    font-size:13px;
                ">
                    {icon} {level}
                </div>

            </div>

            <div style="
                font-family:'Playfair Display';
                font-size:23px;
                line-height:1.6;
                color:#2D3142;
                font-weight:700;
                text-decoration:{underline};
                text-underline-offset:6px;
            ">
                {safe_claim}
            </div>

            <div style="
                margin-top:20px;
                background:rgba(255,255,255,0.55);
                border-left:4px solid {badge_color};
                padding:15px;
                border-radius:12px;
            ">

                <div style="
                    font-family:'Space Grotesk';
                    font-size:13px;
                    color:{badge_color};
                    font-weight:700;
                    margin-bottom:6px;
                ">
                    💡 Why this rating?
                </div>

                <div style="
                    font-family:'Quicksand';
                    font-size:15px;
                    color:#555;
                    line-height:1.5;
                ">
                    {safe_reason}
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------
    # Evidence Section
    # ------------------------------

    if level == "SPECULATIVE":

        st.markdown(
            """
            <div style="
                background:#FFF8E8;
                border:2px dashed #E09B2D;
                border-radius:14px;
                padding:16px;
                margin-top:-10px;
                margin-bottom:20px;
            ">

                <div style="
                    font-family:'Space Grotesk';
                    color:#B45309;
                    font-weight:700;
                    margin-bottom:8px;
                ">
                    ✨ Pure AI Generation
                </div>

                <div style="
                    font-family:'Quicksand';
                    color:#8A5B14;
                    font-size:14px;
                    line-height:1.6;
                ">
                    This statement was generated by the AI without retrieved supporting evidence.
                    Treat it as a creative suggestion, hypothesis, or speculation rather than a verified fact.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        with st.expander("📚 View Supporting Evidence"):

            if not evidence:
                st.info("No supporting evidence was found.")

            else:

                for source in evidence:

                    st.markdown(
                        f"""
                        <div style="
                            background:#FCFCFF;
                            border:1px solid #ECECF4;
                            border-radius:14px;
                            padding:16px;
                            margin-bottom:12px;
                        ">

                            <div style="
                                font-family:'Poppins';
                                font-weight:700;
                                color:#3B3B5C;
                                margin-bottom:6px;
                            ">
                                📖 {html.escape(source.get("title","Source"))}
                            </div>

                            <div style="
                                font-family:'Quicksand';
                                color:#666;
                                line-height:1.5;
                                font-size:14px;
                            ">
                                {html.escape(source.get("content",""))}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if source.get("url"):
                        st.markdown(
                            f"🔗 **[Read Source]({source['url']})**"
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
