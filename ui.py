import streamlit as st


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown("# 🧠 AI Confidence Layer")

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
# FIRST QUESTION INTRO
# ============================================================

def display_first_question():

    st.markdown("## What would you like to know?")

    st.caption(
        "Ask a question and we'll help you understand "
        "how much you can trust the answer."
    )


# ============================================================
# ANALYSIS HEADER
# ============================================================

def display_analysis_header():

    st.markdown("## 🔬 Claim-by-Claim Analysis")

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
    # CONFIDENCE STATUS
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

    st.write(reason)


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

                st.write(content)


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


    st.markdown("## ✦ Trust Overview")


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
