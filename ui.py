import streamlit as st


# ============================================================
# GLOBAL STYLE
# ============================================================

def load_css():

    css = """
<style>

/* ----------------------------------------------------------
   PAGE
---------------------------------------------------------- */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(119, 88, 220, 0.10),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(50, 180, 210, 0.10),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #F7F8FF 0%,
            #F2F5FB 50%,
            #EEF6F8 100%
        );
}


/* ----------------------------------------------------------
   MAIN CONTAINER
---------------------------------------------------------- */

.block-container {
    max-width: 950px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}


/* ----------------------------------------------------------
   TEXT INPUT
---------------------------------------------------------- */

div[data-testid="stTextInput"] input {

    background-color: #FFFFFF !important;

    color: #18233D !important;

    caret-color: #7054D9 !important;

    border: 2px solid #D8DDEA !important;

    border-radius: 16px !important;

    padding: 14px 17px !important;

    font-family:
        'Trebuchet MS',
        Arial,
        sans-serif !important;

    font-size: 16px !important;

    font-weight: 600 !important;

    box-shadow:
        0 6px 18px
        rgba(40, 50, 90, 0.07) !important;
}


div[data-testid="stTextInput"] input:focus {

    background-color: #FFFFFF !important;

    color: #18233D !important;

    border-color: #7054D9 !important;

    box-shadow:
        0 0 0 4px
        rgba(112, 84, 217, 0.12) !important;
}


div[data-testid="stTextInput"] input::placeholder {

    color: #8A94A8 !important;

    opacity: 1 !important;
}


/* ----------------------------------------------------------
   BUTTON
---------------------------------------------------------- */

div.stButton > button,
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
        'Trebuchet MS',
        Arial,
        sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    padding: 10px 22px !important;

    box-shadow:
        0 8px 20px
        rgba(95, 80, 205, 0.22) !important;
}


div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] button:hover {

    background:
        linear-gradient(
            135deg,
            #6847D8,
            #3D7FD2
        ) !important;

    color: #FFFFFF !important;

    border: none !important;
}


/* ----------------------------------------------------------
   EXPANDERS
---------------------------------------------------------- */

div[data-testid="stExpander"] {

    background: rgba(255,255,255,0.88) !important;

    border: 1px solid #DDE3EF !important;

    border-radius: 15px !important;

}


/* ----------------------------------------------------------
   SPINNER
---------------------------------------------------------- */

div[data-testid="stSpinner"] {

    color: #6650C9 !important;

}


/* ----------------------------------------------------------
   WARNING
---------------------------------------------------------- */

div[data-testid="stAlert"] {

    border-radius: 14px !important;

}

</style>
"""

    # IMPORTANT:
    # The <style> tag starts at the very beginning of the string.
    # Do NOT indent this string.

    st.markdown(css, unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown(
        """
# 🧠 AI Confidence Layer
""",
        unsafe_allow_html=False
    )

    st.markdown(
        """
### Don't just get an AI answer.
#### Understand **why you should trust it.**
""",
        unsafe_allow_html=False
    )

    st.caption(
        "Evidence • Claim Analysis • Trust Signals"
    )

    st.divider()


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
    # HIGH
    # --------------------------------------------------------

    if level == "HIGH":

        st.success(
            "🟢 STRONGLY SUPPORTED"
        )


    # --------------------------------------------------------
    # MEDIUM
    # --------------------------------------------------------

    elif level == "MEDIUM":

        st.warning(
            "🟡 PARTIALLY SUPPORTED"
        )


    # --------------------------------------------------------
    # LOW / SPECULATIVE
    # --------------------------------------------------------

    else:

        st.markdown(
            """
**🟠 PURE GENERATION · SPECULATIVE**

*No retrieved source was found to directly support this claim.*
"""
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

    st.write(reason)


    # --------------------------------------------------------
    # EVIDENCE
    # --------------------------------------------------------

    with st.expander(
        "▸ View Supporting Evidence"
    ):

        if not evidence:

            st.markdown(
                """
**🟠 Pure Generation / Speculative**

No retrieved source was found for this claim.

Treat this information cautiously.
"""
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
                    f"### ◈ {title}"
                )

                st.write(content)

                if url:

                    st.markdown(
                        f"[Open source ↗]({url})"
                    )

                st.divider()


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
# FOLLOW-UP QUESTION PROMPT
# ============================================================

def display_question_prompt():

    st.divider()

    st.markdown(
        "## ✨ What would you like to know next?"
    )

    st.write(
        "Ask something related to your previous question "
        "or explore a completely different topic."
    )
