import streamlit as st


# ---------------------------------------------------------
# PAGE STYLING
# ---------------------------------------------------------

def load_css():
    st.markdown("""
    <style>

    /* Main page */
    .stApp {
        background: linear-gradient(135deg, #0b1020 0%, #111827 50%, #0f172a 100%);
        color: #f8fafc;
    }

    /* Main content width */
    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Header */
    .hero {
        text-align: center;
        padding: 35px 20px 30px 20px;
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #ffffff, #a5b4fc);
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

    /* Confidence cards */
    .claim-card {
        background: rgba(30, 41, 59, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        backdrop-filter: blur(10px);
    }

    .claim-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 18px;
    }

    .confidence-badge {
        padding: 7px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    .confidence-high {
        background: rgba(34, 197, 94, 0.15);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.35);
    }

    .confidence-medium {
        background: rgba(234, 179, 8, 0.15);
        color: #facc15;
        border: 1px solid rgba(234, 179, 8, 0.35);
    }

    .confidence-low {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.35);
    }

    .claim-text {
        font-size: 19px;
        font-weight: 500;
        line-height: 1.6;
        color: #f8fafc;
        margin-bottom: 18px;
    }

    .reason-box {
        background: rgba(15, 23, 42, 0.7);
        border-radius: 12px;
        padding: 14px 16px;
        border-left: 3px solid #818cf8;
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.5;
    }

    .reason-title {
        color: #a5b4fc;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Evidence cards */
    .evidence-card {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
    }

    .evidence-title {
        font-weight: 700;
        color: #e2e8f0;
        margin-bottom: 7px;
    }

    .evidence-text {
        color: #94a3b8;
        font-size: 14px;
        line-height: 1.5;
    }

    /* Section title */
    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 35px;
        margin-bottom: 15px;
    }

    /* Streamlit buttons */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: 700;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35);
    }

    /* Text input */
    .stTextInput input {
        border-radius: 12px;
        background: rgba(30, 41, 59, 0.8);
        color: white;
        border: 1px solid rgba(148, 163, 184, 0.25);
        padding: 13px;
    }

    /* Expander */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #cbd5e1;
    }

    /* Divider */
    hr {
        border-color: rgba(148, 163, 184, 0.12);
    }

    </style>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

def display_header():

    st.title("🧠 AI Confidence Layer")

    st.caption(
        "Don't just get an AI answer. "
        "Understand why you should trust it."
    )


# ---------------------------------------------------------
# CLAIM DISPLAY
# ---------------------------------------------------------

def display_claim(claim, confidence, evidence):

    level = confidence.get("confidence", "LOW").upper()
    reason = confidence.get(
        "reason",
        "There is not enough information to determine confidence."
    )

    # Choose badge styling
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
        f"""
        <div class="claim-card">

            <div class="claim-header">

                <div style="
                    color:#64748b;
                    font-size:13px;
                    font-weight:600;
                    text-transform:uppercase;
                    letter-spacing:1px;
                ">
                    AI Claim
                </div>

                <div class="confidence-badge {badge_class}">
                    {icon} {label}
                </div>

            </div>

            <div class="claim-text">
                {claim}
            </div>

            <div class="reason-box">

                <div class="reason-title">
                    🔍 Why this rating?
                </div>

                {reason}

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Evidence section
    with st.expander("📚 View supporting evidence"):

        if not evidence:

            st.info(
                "No supporting evidence was found for this claim."
            )

        else:

            for source in evidence:

                title = source.get(
                    "title",
                    "Source"
                )

                content = source.get(
                    "content",
                    "No source description available."
                )

                url = source.get(
                    "url",
                    "#"
                )

                st.markdown(
                    f"""
                    <div class="evidence-card">

                        <div class="evidence-title">
                            📄 {title}
                        </div>

                        <div class="evidence-text">
                            {content}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if url != "#":
                    st.markdown(
                        f"[🔗 Open source]({url})"
                    )

    st.markdown("<br>", unsafe_allow_html=True)


# ---------------------------------------------------------
# OVERALL SUMMARY
# ---------------------------------------------------------

def display_summary(claims_data):

    if not claims_data:
        return

    total = len(claims_data)

    high = sum(
        1 for item in claims_data
        if item["confidence"]["confidence"].upper() == "HIGH"
    )

    medium = sum(
        1 for item in claims_data
        if item["confidence"]["confidence"].upper() == "MEDIUM"
    )

    low = sum(
        1 for item in claims_data
        if item["confidence"]["confidence"].upper() == "LOW"
    )

    st.markdown(
        '<div class="section-title">📊 Trust Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Claims", total)

    with col2:
        st.metric("🟢 High", high)

    with col3:
        st.metric("🟡 Medium", medium)

    with col4:
        st.metric("🔴 Low", low)
