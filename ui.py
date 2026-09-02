import streamlit as st


def display_claim(claim, confidence, evidence):

    level = confidence["confidence"]

    if level == "HIGH":
        icon = "🟢"
    elif level == "MEDIUM":
        icon = "🟡"
    else:
        icon = "🔴"

    st.markdown(
        f"### {icon} {level} CONFIDENCE"
    )

    st.write(claim)

    st.write(
        f"**Why:** {confidence['reason']}"
    )

    with st.expander("View evidence"):

        for source in evidence:

            st.markdown(
                f"**{source['title']}**"
            )

            st.write(source["content"])

            st.markdown(
                f"[Open source]({source['url']})"
            )

    st.divider()
