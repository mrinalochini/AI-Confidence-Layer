import streamlit as st
import html


# ============================================================
# GLOBAL CSS
# ============================================================

def load_css():

    st.markdown(
        """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 10%, rgba(126, 92, 230, 0.10), transparent 25%),
        radial-gradient(circle at 95% 15%, rgba(45, 190, 220, 0.10), transparent 25%),
        linear-gradient(135deg, #F7F8FF, #EEF4FA);
}

.block-container {
    max-width: 980px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}

/* QUESTION INPUT */

div[data-testid="stTextInput"] label {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #34405C !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}

div[data-testid="stTextInput"] input {
    background: #FFFFFF !important;
    color: #17233F !important;
    caret-color: #7655E8 !important;
    border: 1.5px solid #D7DBEA !important;
    border-radius: 16px !important;
    padding: 14px 17px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    box-shadow: 0 7px 20px rgba(40, 50, 80, 0.07) !important;
}

div[data-testid="stTextInput"] input:focus {
    border: 1.5px solid #7655E8 !important;
    box-shadow: 0 0 0 4px rgba(118, 85, 232, 0.12) !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #8D96A9 !important;
}

/* BUTTON */

div.stButton > button {
    background: linear-gradient(135deg, #7655E8, #4E8DDE) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    padding: 10px 22px !important;
    box-shadow: 0 8px 20px rgba(100, 85, 210, 0.25) !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #6746D8, #3D7FD2) !important;
    color: white !important;
    transform: translateY(-2px);
}

/* EXPANDER */

div[data-testid="stExpander"] {
    background: rgba(255,255,255,0.85) !important;
    border: 1px solid #DEE3EF !important;
    border-radius: 14px !important;
}

div[data-testid="stExpander"] summary {
    color: #35415C !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
}

</style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

def display_header():

    st.markdown(
        """
<div style="
    background:linear-gradient(145deg,#FFFFFF,#F4F0FF,#EEF9FF);
    border:1px solid #DEE2F0;
    border-radius:28px;
    padding:42px 30px 36px;
    text-align:center;
    margin-bottom:40px;
    box-shadow:0 18px 45px rgba(40,50,90,0.09);
">

<div style="
    font-size:46px;
    margin-bottom:10px;
">🧠</div>

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    letter-spacing:2.5px;
    color:#7967B8;
    margin-bottom:10px;
">
INTELLIGENCE · EVIDENCE · TRUST
</div>

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:42px;
    font-weight:700;
    color:#18243F;
    line-height:1.15;
">
AI Confidence
<span style="color:#7655E8;">Layer</span>
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    color:#69758C;
    font-size:16px;
    margin-top:14px;
    line-height:1.6;
">
Don't just get an AI answer.
<br>
<span style="color:#6749D7;font-weight:700;">
Understand why you should trust it.
</span>
</div>

<div style="margin-top:20px;">

<span style="
    display:inline-block;
    background:#EFEAFF;
    color:#6549D0;
    padding:7px 12px;
    border-radius:20px;
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    margin:4px;
">
✦ CLAIM ANALYSIS
</span>

<span style="
    display:inline-block;
    background:#E6F7FB;
    color:#277D96;
    padding:7px 12px;
    border-radius:20px;
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    margin:4px;
">
◈ EVIDENCE
</span>

<span style="
    display:inline-block;
    background:#FFF1D4;
    color:#986919;
    padding:7px 12px;
    border-radius:20px;
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    margin:4px;
">
◉ TRUST SIGNAL
</span>

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
<div style="
    margin-top:35px;
    margin-bottom:18px;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    letter-spacing:1.5px;
    color:#8274AE;
">
TRUST ENGINE
</div>

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:25px;
    font-weight:700;
    color:#25314B;
    margin-top:3px;
">
◈ Claim-by-Claim Analysis
</div>

</div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CLAIM DISPLAY
# ============================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get("confidence", "LOW")
    reason = confidence.get(
        "reason",
        "There is insufficient evidence to determine this claim."
    )

    safe_claim = html.escape(str(claim))
    safe_reason = html.escape(str(reason))


    if level == "HIGH":

        badge = "✓ STRONGLY SUPPORTED"
        badge_color = "#218153"
        badge_bg = "#E8F8EF"
        border = "#CDEBDD"

    elif level == "MEDIUM":

        badge = "◐ PARTIALLY SUPPORTED"
        badge_color = "#9A6918"
        badge_bg = "#FFF5DE"
        border = "#F0D9A2"

    else:

        badge = "◇ PURE GENERATION · SPECULATIVE"
        badge_color = "#95651A"
        badge_bg = "#FFF2D8"
        border = "#DDBE78"


    # CLAIM CARD

    st.markdown(
        f"""
<div style="
    background:#FFFFFF;
    border:1px solid {border};
    border-radius:20px;
    padding:24px;
    margin-bottom:15px;
    box-shadow:0 8px 25px rgba(40,50,80,0.06);
">

<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
    margin-bottom:15px;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    letter-spacing:1.4px;
    color:#8992A7;
">
AI CLAIM
</div>

<div style="
    background:{badge_bg};
    color:{badge_color};
    padding:7px 11px;
    border-radius:30px;
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
">
{badge}
</div>

</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:18px;
    font-weight:600;
    line-height:1.65;
    color:#26324B;
    margin-bottom:18px;
">
{safe_claim}
</div>

<div style="
    background:linear-gradient(135deg,#F7F4FF,#F1FAFC);
    border:1px solid #E7E6F1;
    border-radius:14px;
    padding:15px 17px;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:9px;
    font-weight:700;
    letter-spacing:1.2px;
    color:#7968B3;
    margin-bottom:6px;
">
WHY THIS RATING?
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:14px;
    line-height:1.6;
    color:#667188;
">
{safe_reason}
</div>

</div>

</div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # EVIDENCE
    # ========================================================

    with st.expander("▸  View Supporting Evidence"):

        if not evidence:

            st.markdown(
                """
<div style="
    background:#FFF8E9;
    border:1px dashed #D8B96D;
    border-radius:14px;
    padding:17px;
    color:#8B681D;
    font-family:'DM Sans',sans-serif;
    font-size:14px;
">
◇ No retrieved source was found for this claim.<br><br>
This claim should therefore be treated as
<b>pure generation / speculative</b>.
</div>
                """,
                unsafe_allow_html=True
            )

        else:

            for source in evidence:

                title = html.escape(
                    str(source.get("title", "Source"))
                )

                content = html.escape(
                    str(source.get("content", "No content available."))
                )

                url = html.escape(
                    str(source.get("url", "#"))
                )

                st.markdown(
                    f"""
<div style="
    background:#F8FBFE;
    border:1px solid #DDE7EF;
    border-radius:14px;
    padding:16px;
    margin-bottom:12px;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:14px;
    font-weight:700;
    color:#2C405D;
    margin-bottom:8px;
">
◈ {title}
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:13px;
    line-height:1.6;
    color:#69758A;
    margin-bottom:10px;
">
{content}
</div>

<a href="{url}" target="_blank"
style="
    color:#674DD3;
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    text-decoration:none;
">
OPEN SOURCE ↗
</a>

</div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# SUMMARY
# ============================================================

def display_summary(analyzed_claims):

    total = len(analyzed_claims)

    high = sum(
        1 for x in analyzed_claims
        if x["confidence"].get("confidence") == "HIGH"
    )

    medium = sum(
        1 for x in analyzed_claims
        if x["confidence"].get("confidence") == "MEDIUM"
    )

    low = sum(
        1 for x in analyzed_claims
        if x["confidence"].get("confidence") == "LOW"
    )


    st.markdown(
        f"""
<div style="
    margin-top:25px;
    margin-bottom:12px;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:10px;
    font-weight:700;
    letter-spacing:1.5px;
    color:#8179A4;
    margin-bottom:10px;
">
TRUST OVERVIEW
</div>

<div style="
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:10px;
">

<div style="
    background:#FFFFFF;
    border:1px solid #E0E4EF;
    border-radius:15px;
    padding:15px;
    text-align:center;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:23px;
    font-weight:700;
    color:#293550;
">
{total}
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:10px;
    font-weight:600;
    color:#8790A5;
">
CLAIMS
</div>

</div>


<div style="
    background:#EFFAF4;
    border:1px solid #D4EDDE;
    border-radius:15px;
    padding:15px;
    text-align:center;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:23px;
    font-weight:700;
    color:#218153;
">
{high}
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:10px;
    font-weight:600;
    color:#5D9277;
">
STRONG
</div>

</div>


<div style="
    background:#FFF8E9;
    border:1px solid #F0DFB5;
    border-radius:15px;
    padding:15px;
    text-align:center;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:23px;
    font-weight:700;
    color:#9A6B1B;
">
{medium}
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:10px;
    font-weight:600;
    color:#9A7B3D;
">
PARTIAL
</div>

</div>


<div style="
    background:#FFF4E2;
    border:1px dashed #DDBE78;
    border-radius:15px;
    padding:15px;
    text-align:center;
">

<div style="
    font-family:'Space Grotesk',sans-serif;
    font-size:23px;
    font-weight:700;
    color:#96671B;
">
{low}
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:10px;
    font-weight:600;
    color:#997A3D;
">
SPECULATIVE
</div>

</div>

</div>
</div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOLLOW-UP QUESTION
# ============================================================

def display_question_prompt():

    st.markdown(
        """
<div style="
    margin-top:48px;
    margin-bottom:15px;
    padding:28px 24px;
    text-align:center;
    background:linear-gradient(145deg,#FFFFFF,#F5F1FF,#EEF9FF);
    border:1px solid #DEE3EF;
    border-radius:22px;
    box-shadow:0 10px 30px rgba(40,50,80,0.06);
">

<div style="font-size:28px;margin-bottom:6px;">
✨
</div>

<div style="
    font-family:'Playfair Display',serif;
    font-size:26px;
    font-weight:600;
    color:#293550;
">
What would you like to know next?
</div>

<div style="
    font-family:'DM Sans',sans-serif;
    font-size:14px;
    color:#758096;
    margin-top:7px;
    line-height:1.6;
">
Ask something related to your previous question
or explore a completely different topic.
</div>

</div>
        """,
        unsafe_allow_html=True
    )
