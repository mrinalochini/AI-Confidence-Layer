import streamlit as st
import html
import textwrap


# =========================================================
# PAGE STYLING
# =========================================================

def load_css():

    st.markdown(
        textwrap.dedent("""
        <style>

        /* ==============================
           MAIN APP
        ============================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 20% 0%,
                    rgba(99, 102, 241, 0.16),
                    transparent 35%
                ),
                radial-gradient(
                    circle at 90% 10%,
                    rgba(139, 92, 246, 0.12),
                    transparent 30%
                ),
                #080d1b;

            color: #f8fafc;
        }


        .block-container {
            max-width: 1050px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }


        /* ==============================
           HERO
           ============================== */

        .hero {
            text-align: center;
            padding: 45px 20px 35px 20px;
        }


        .hero-icon {
            font-size: 42px;
            margin-bottom: 8px;
        }


        .hero-title {
            font-size: 48px;
            font-weight: 800;
            letter-spacing: -1.5px;
            margin-bottom: 10px;

            background: linear-gradient(
                90deg,
                #ffffff,
                #c4b5fd,
                #818cf8
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }


        .hero-subtitle {
            font-size: 18px;
            color: #94a3b8;
            max-width: 650px;
            margin: auto;
            line-height: 1.6;
        }


        /* ==============================
           QUESTION AREA
           ============================== */

        .question-label {
            font-size: 14px;
            font-weight: 700;
            color: #cbd5e1;
            margin-bottom: 8px;
        }


        /* ==============================
           SECTION HEADERS
           ============================== */

        .section-header {
            display: flex;
            align-items: center;
            gap: 10px;

            font-size: 27px;
            font-weight: 750;

            color: #f8fafc;

            margin-top: 42px;
            margin-bottom: 18px;
        }


        .section-description {
            color: #64748b;
            font-size: 14px;
            margin-top: -10px;
            margin-bottom: 20px;
        }


        /* ==============================
           CLAIM CARD
           ============================== */

        .claim-card {

            background: linear-gradient(
                145deg,
                rgba(30, 41, 59, 0.92),
                rgba(15, 23, 42, 0.92)
            );

            border: 1px solid rgba(148, 163, 184, 0.16);

            border-radius: 20px;

            padding: 25px;

            margin: 18px 0;

            box-shadow:
                0 15px 40px rgba(0, 0, 0, 0.25);

            transition: all 0.2s ease;
        }


        .claim-card:hover {

            border-color:
                rgba(129, 140, 248, 0.35);

            transform: translateY(-2px);

            box-shadow:
                0 20px 45px rgba(0, 0, 0, 0.32);
        }


        .claim-header {

            display: flex;

            justify-content: space-between;

            align-items: center;

            margin-bottom: 20px;
        }


        .claim-number {

            color: #64748b;

            font-size: 12px;

            font-weight: 800;

            text-transform: uppercase;

            letter-spacing: 1.3px;
        }


        /* ==============================
           CONFIDENCE BADGES
           ============================== */

        .confidence-badge {

            padding: 7px 13px;

            border-radius: 999px;

            font-size: 12px;

            font-weight: 800;

            letter-spacing: 0.5px;
        }


        .confidence-high {

            background:
                rgba(34, 197, 94, 0.12);

            color: #4ade80;

            border:
                1px solid rgba(34, 197, 94, 0.30);
        }


        .confidence-medium {

            background:
                rgba(234, 179, 8, 0.12);

            color: #facc15;

            border:
                1px solid rgba(234, 179, 8, 0.30);
        }


        .confidence-low {

            background:
                rgba(239, 68, 68, 0.12);

            color: #f87171;

            border:
                1px solid rgba(239, 68, 68, 0.30);
        }


        /* ==============================
           CLAIM TEXT
           ============================== */

        .claim-text {

            font-size: 20px;

            font-weight: 550;

            line-height: 1.65;

            color: #f8fafc;

            margin-bottom: 20px;
        }


        /* ==============================
           WHY BOX
           ============================== */

        .reason-box {

            background:
                rgba(2, 6, 23, 0.55);

            border:
                1px solid rgba(148, 163, 184, 0.10);

            border-left:
                3px solid #818cf8;

            border-radius: 12px;

            padding: 15px 17px;

            color: #cbd5e1;

            font-size: 14px;

            line-height: 1.6;
        }


        .reason-title {

            color: #a5b4fc;

            font-weight: 750;

            margin-bottom: 5px;
        }


        /* ==============================
           EVIDENCE CARDS
           ============================== */

        .evidence-card {

            background:
                rgba(15, 23, 42, 0.72);

            border:
                1px solid rgba(148, 163, 184, 0.12);

            border-radius: 14px;

            padding: 17px;

            margin: 12px 0;
        }


        .evidence-title {

            color: #e2e8f0;

            font-weight: 700;

            font-size: 15px;

            margin-bottom: 8px;
        }


        .evidence-text {

            color: #94a3b8;

            font-size: 14px;

            line-height: 1.6;
        }


        /* ==============================
           SUMMARY
           ============================== */

        .summary-card {

            background:
                linear-gradient(
                    145deg,
                    rgba(30, 41, 59, 0.85),
                    rgba(15, 23, 42, 0.85)
                );

            border:
                1px solid rgba(148, 163, 184, 0.14);

            border-radius: 18px;

            padding: 22px;

            text-align: center;

            min-height: 105px;
        }


        .summary-number {

            font-size: 28px;

            font-weight: 800;

            color: #f8fafc;
        }


        .summary-label {

            font-size: 12px;

            color: #64748b;

            font-weight: 700;

            text-transform: uppercase;

            letter-spacing: 0.8px;

            margin-top: 3px;
        }


        /* ==============================
           BUTTON
           ============================== */

        .stButton > button {

            width: 100%;

            border-radius: 13px;

            border: 1px solid
                rgba(139, 92, 246, 0.4);

            padding: 12px 20px;

            font-size: 16px;

            font-weight: 750;

            background:
                linear-gradient(
                    90deg,
                    #6366f1,
                    #8b5cf6
                );

            color: white;

            transition: all 0.2s ease;
        }


        .stButton > button:hover {

            transform: translateY(-2px);

            box-shadow:
                0 10px 25px
                rgba(99, 102, 241, 0.30);
        }


        /* ==============================
           TEXT INPUT
           ============================== */

        .stTextInput input {

            border-radius: 13px;

            background:
                rgba(30, 41, 59, 0.75);

            color: white;

            border:
                1px solid
                rgba(148, 163, 184, 0.20);

            padding: 13px 15px;

            font-size: 15px;
        }


        .stTextInput input:focus {

            border-color:
                rgba(129, 140, 248, 0.65);

            box-shadow:
                0 0 0 1px
                rgba(129, 140, 248, 0.25);
        }


        /* ==============================
           EXPANDER
           ============================== */

        .streamlit-expanderHeader {

            color: #cbd5e1 !important;

            font-weight: 700 !important;
        }


        /* ==============================
           DIVIDER
           ============================== */

        hr {

            border-color:
                rgba(148, 163, 184, 0.10);
        }


        </style>
        """),
        unsafe_allow_html=True
    )


# =========================================================
# HEADER
# =========================================================

def display_header():

    st.markdown(
        textwrap.dedent("""
        <div class="hero">

            <div class="hero-icon">
                🧠
            </div>

            <div class="hero-title">
                AI Confidence Layer
            </div>

            <div class="hero-subtitle">
                Don't just get an AI answer.
                Understand <b>why you should trust it.</b>
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


# =========================================================
# CLAIM DISPLAY
# =========================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get(
        "confidence",
        "LOW"
    ).upper()

    reason = confidence.get(
        "reason",
        "There is not enough evidence to determine confidence."
    )


    # Safely escape dynamic content
    safe_claim = html.escape(str(claim))
    safe_reason = html.escape(str(reason))


    # Choose confidence styling

    if level == "HIGH":

        icon = "🟢"
        badge_class = "confidence-high"
        label = "HIGH CONFIDENCE"

    elif level == "MEDIUM":

        icon = "🟡"
        badge_class = "confidence-medium"
        label = "MEDIUM CONFIDENCE"

    else:

        icon = "🔴"
        badge_class = "confidence-low"
        label = "LOW CONFIDENCE"


    # Claim card

    st.markdown(
        textwrap.dedent(
            f"""
            <div class="claim-card">

                <div class="claim-header">

                    <div class="claim-number">
                        AI CLAIM
                    </div>

                    <div class="confidence-badge {badge_class}">
                        {icon} {label}
                    </div>

                </div>

                <div class="claim-text">
                    {safe_claim}
                </div>

                <div class="reason-box">

                    <div class="reason-title">
                        🔍 Why this rating?
                    </div>

                    {safe_reason}

                </div>

            </div>
            """
        ),
        unsafe_allow_html=True
    )


    # Evidence

    with st.expander("📚  View supporting evidence"):

        if not evidence:

            st.warning(
                "No supporting evidence was found for this claim."
            )

        else:

            for source in evidence:

                title = html.escape(
                    str(
                        source.get(
                            "title",
                            "Source"
                        )
                    )
                )

                content = html.escape(
                    str(
                        source.get(
                            "content",
                            "No source description available."
                        )
                    )
                )

                url = source.get(
                    "url",
                    "#"
                )


                st.markdown(
                    textwrap.dedent(
                        f"""
                        <div class="evidence-card">

                            <div class="evidence-title">
                                📄 {title}
                            </div>

                            <div class="evidence-text">
                                {content}
                            </div>

                        </div>
                        """
                    ),
                    unsafe_allow_html=True
                )


                if url != "#":

                    st.markdown(
                        f"[🔗 Open source]({url})"
                    )


# =========================================================
# OVERALL SUMMARY
# =========================================================

def display_summary(claims_data):

    if not claims_data:
        return


    total = len(claims_data)


    high = sum(
        1
        for item in claims_data
        if item["confidence"]
        .get("confidence", "LOW")
        .upper() == "HIGH"
    )


    medium = sum(
        1
        for item in claims_data
        if item["confidence"]
        .get("confidence", "LOW")
        .upper() == "MEDIUM"
    )


    low = sum(
        1
        for item in claims_data
        if item["confidence"]
        .get("confidence", "LOW")
        .upper() == "LOW"
    )


    # Section title

    st.markdown(
        textwrap.dedent("""
        <div class="section-header">
            📊 Trust Summary
        </div>

        <div class="section-description">
            A quick overview of how well the generated claims
            are supported by external evidence.
        </div>
        """),
        unsafe_allow_html=True
    )


    # Summary cards

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            textwrap.dedent(
                f"""
                <div class="summary-card">

                    <div class="summary-number">
                        {total}
                    </div>

                    <div class="summary-label">
                        Total Claims
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            textwrap.dedent(
                f"""
                <div class="summary-card">

                    <div class="summary-number">
                        🟢 {high}
                    </div>

                    <div class="summary-label">
                        High
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            textwrap.dedent(
                f"""
                <div class="summary-card">

                    <div class="summary-number">
                        🟡 {medium}
                    </div>

                    <div class="summary-label">
                        Medium
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            textwrap.dedent(
                f"""
                <div class="summary-card">

                    <div class="summary-number">
                        🔴 {low}
                    </div>

                    <div class="summary-label">
                        Low
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


# =========================================================
# CLAIM ANALYSIS HEADER
# =========================================================

def display_analysis_header():

    st.markdown(
        textwrap.dedent("""
        <div class="section-header">
            🔬 Claim-by-Claim Analysis
        </div>

        <div class="section-description">
            Each statement is evaluated against external evidence
            before a trust rating is assigned.
        </div>
        """),
        unsafe_allow_html=True
    )
