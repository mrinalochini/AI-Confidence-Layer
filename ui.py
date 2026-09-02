import html
import textwrap
import streamlit as st


# =========================================================
# SAFE HTML RENDERER
# =========================================================

def render_html(content):
    """
    Safely removes indentation from multiline HTML
    before sending it to Streamlit.
    
    This prevents Streamlit from displaying HTML
    as a code block.
    """

    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True
    )


# =========================================================
# PAGE STYLING
# =========================================================

def load_css():

    css = """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&family=Quicksand:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');


    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 214, 240, 0.45),
                transparent 30%
            ),

            radial-gradient(
                circle at 90% 15%,
                rgba(211, 231, 255, 0.55),
                transparent 32%
            ),

            radial-gradient(
                circle at 50% 100%,
                rgba(255, 235, 190, 0.40),
                transparent 35%
            ),

            #F8F9FF;

        color: #20263A;

    }


    /* =====================================================
       REMOVE STREAMLIT TOP PADDING
       ===================================================== */

    .block-container {

        max-width: 950px !important;

        padding-top: 2rem !important;

        padding-bottom: 4rem !important;

    }


    /* =====================================================
       QUESTION INPUT
       ===================================================== */

    div[data-baseweb="input"] {

        background: #FFFFFF !important;

        border: 2px solid #D9DCEF !important;

        border-radius: 17px !important;

        box-shadow:
            0 6px 20px rgba(79, 88, 140, 0.08) !important;

    }


    div[data-baseweb="input"]:focus-within {

        border-color: #8A63E8 !important;

        box-shadow:
            0 0 0 4px rgba(138, 99, 232, 0.12),
            0 8px 25px rgba(79, 88, 140, 0.10) !important;

    }


    input {

        color: #20263A !important;

        -webkit-text-fill-color: #20263A !important;

        font-family:
            "DM Sans",
            sans-serif !important;

        font-size: 16px !important;

        font-weight: 500 !important;

    }


    input::placeholder {

        color: #8D94A8 !important;

        opacity: 1 !important;

    }


    /* =====================================================
       ANALYZE BUTTON
       ===================================================== */

    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {

        background:
            linear-gradient(
                135deg,
                #7654E8,
                #A34FD1,
                #4C8FE8
            ) !important;

        color: #FFFFFF !important;

        -webkit-text-fill-color: #FFFFFF !important;

        border: none !important;

        border-radius: 15px !important;

        min-height: 52px !important;

        padding:
            10px 28px !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        box-shadow:
            0 8px 22px rgba(106, 77, 210, 0.25) !important;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease !important;

    }


    .stButton > button p,
    div[data-testid="stFormSubmitButton"] > button p {

        color: #FFFFFF !important;

        -webkit-text-fill-color: #FFFFFF !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-weight: 700 !important;

    }


    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {

        background:
            linear-gradient(
                135deg,
                #6946DC,
                #963DC5,
                #3E82DD
            ) !important;

        transform: translateY(-2px);

        box-shadow:
            0 12px 28px rgba(106, 77, 210, 0.32) !important;

    }


    /* =====================================================
       EXPANDER
       ===================================================== */

    div[data-testid="stExpander"] {

        background: #FFFFFF !important;

        border:
            1px solid #E2E5F0 !important;

        border-radius: 16px !important;

        margin-top: 14px !important;

        box-shadow:
            0 5px 18px rgba(70, 76, 120, 0.06) !important;

    }


    div[data-testid="stExpander"] summary {

        color: #414960 !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-size: 14px !important;

        font-weight: 700 !important;

    }


    /* =====================================================
       STREAMLIT DIVIDER
       ===================================================== */

    hr {

        border-color: #E5E7F0 !important;

    }


    </style>
    """

    render_html(css)


# =========================================================
# HEADER
# =========================================================

def display_header():

    render_html(
        """
        <div style="
            background:
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #F8F3FF 48%,
                    #EEF7FF 100%
                );

            border:
                1px solid #E3E1F2;

            border-radius: 28px;

            padding:
                42px 35px;

            margin-bottom: 38px;

            text-align: center;

            box-shadow:
                0 14px 40px rgba(84, 91, 140, 0.10);
        ">

            <div style="
                font-size: 48px;
                margin-bottom: 12px;
            ">
                🧠✨
            </div>

            <div style="
                font-family: 'Playfair Display', serif;
                font-size: 44px;
                font-weight: 700;
                color: #20263A;
                line-height: 1.15;
                margin-bottom: 15px;
            ">
                AI Confidence Layer
            </div>

            <div style="
                font-family: 'Quicksand', sans-serif;
                font-size: 18px;
                color: #687089;
                line-height: 1.6;
            ">
                Don't just get an AI answer.
                <span style="
                    color: #7654E8;
                    font-weight: 700;
                ">
                    Understand why you should trust it.
                </span>
            </div>

        </div>
        """
    )


# =========================================================
# ANALYSIS HEADER
# =========================================================

def display_analysis_header():

    render_html(
        """
        <div style="
            margin-top: 38px;
            margin-bottom: 20px;
        ">

            <div style="
                font-family: 'Playfair Display', serif;
                font-size: 29px;
                font-weight: 700;
                color: #20263A;
            ">
                🔬 Claim-by-Claim Analysis
            </div>

            <div style="
                font-family: 'Quicksand', sans-serif;
                font-size: 14px;
                color: #7B8297;
                margin-top: 5px;
            ">
                See exactly which parts of the answer deserve your trust.
            </div>

        </div>
        """
    )


# =========================================================
# CLAIM CARD
# =========================================================

def display_claim(claim, confidence, evidence):

    level = str(
        confidence.get(
            "confidence",
            "LOW"
        )
    ).upper()

    reason = confidence.get(
        "reason",
        "No explanation was provided."
    )


    safe_claim = html.escape(
        str(claim)
    )

    safe_reason = html.escape(
        str(reason)
    )


    # =====================================================
    # HIGH
    # =====================================================

    if level == "HIGH":

        icon = "🟢"

        badge_text = "HIGH CONFIDENCE"

        badge_bg = "#E7F9EF"

        badge_color = "#168A4A"

        card_background = (
            "linear-gradient("
            "135deg,"
            "#FFFFFF 0%,"
            "#F1FFF7 100%"
            ")"
        )

        border_color = "#CBEFD9"

        title = "Evidence-backed claim"

        claim_color = "#25334A"

        underline = "none"


    # =====================================================
    # MEDIUM
    # =====================================================

    elif level == "MEDIUM":

        icon = "🔵"

        badge_text = "MEDIUM CONFIDENCE"

        badge_bg = "#EAF3FF"

        badge_color = "#2874C7"

        card_background = (
            "linear-gradient("
            "135deg,"
            "#FFFFFF 0%,"
            "#F1F8FF 100%"
            ")"
        )

        border_color = "#D2E5FA"

        title = "Partially supported claim"

        claim_color = "#25334A"

        underline = "none"


    # =====================================================
    # SPECULATIVE
    # =====================================================

    elif level == "SPECULATIVE":

        icon = "✨"

        badge_text = "PURE GENERATION"

        badge_bg = "#FFF1C9"

        badge_color = "#A86408"

        card_background = (
            "linear-gradient("
            "135deg,"
            "#FFFDF7 0%,"
            "#FFF2D2 100%"
            ")"
        )

        border_color = "#F1D18A"

        title = "AI-generated insight"

        claim_color = "#493716"

        underline = (
            "text-decoration: underline;"
            "text-decoration-style: dashed;"
            "text-decoration-color: #D68B18;"
            "text-decoration-thickness: 3px;"
            "text-underline-offset: 7px;"
        )


    # =====================================================
    # LOW
    # =====================================================

    else:

        icon = "🔴"

        badge_text = "LOW CONFIDENCE"

        badge_bg = "#FFEAEA"

        badge_color = "#C83C3C"

        card_background = (
            "linear-gradient("
            "135deg,"
            "#FFFFFF 0%,"
            "#FFF5F5 100%"
            ")"
        )

        border_color = "#F1CCCC"

        title = "Weakly supported claim"

        claim_color = "#4A2A2A"

        underline = "none"


    # =====================================================
    # CLAIM CARD HTML
    # =====================================================

    render_html(
        f"""
        <div style="
            background: {card_background};

            border:
                1px solid {border_color};

            border-radius: 23px;

            padding: 25px 27px;

            margin-bottom: 18px;

            box-shadow:
                0 10px 28px
                rgba(70, 76, 120, 0.07);
        ">

            <div style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 15px;
                margin-bottom: 18px;
            ">

                <div style="
                    font-family:
                        'Space Grotesk',
                        sans-serif;

                    font-size: 12px;

                    letter-spacing: 1.3px;

                    text-transform: uppercase;

                    color: #7A8195;

                    font-weight: 700;
                ">
                    {title}
                </div>

                <div style="
                    background: {badge_bg};

                    color: {badge_color};

                    border-radius: 999px;

                    padding:
                        8px 13px;

                    font-family:
                        'Space Grotesk',
                        sans-serif;

                    font-size: 12px;

                    font-weight: 700;

                    white-space: nowrap;
                ">
                    {icon} {badge_text}
                </div>

            </div>


            <div style="
                font-family:
                    'DM Sans',
                    sans-serif;

                font-size: 21px;

                line-height: 1.65;

                color: {claim_color};

                font-weight: 600;

                {underline}
            ">
                {safe_claim}
            </div>


            <div style="
                margin-top: 21px;

                background:
                    rgba(255,255,255,0.68);

                border-left:
                    4px solid {badge_color};

                border-radius: 12px;

                padding:
                    14px 16px;
            ">

                <div style="
                    font-family:
                        'Space Grotesk',
                        sans-serif;

                    color: {badge_color};

                    font-size: 12px;

                    font-weight: 700;

                    letter-spacing: 0.6px;

                    margin-bottom: 5px;
                ">
                    💡 WHY THIS RATING?
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

                    color: #5D6475;

                    font-size: 14px;

                    line-height: 1.6;

                    font-weight: 500;
                ">
                    {safe_reason}
                </div>

            </div>

        </div>
        """
    )


    # =====================================================
    # SPECULATIVE NOTICE
    # =====================================================

    if level == "SPECULATIVE":

        render_html(
            """
            <div style="
                background: #FFF9EA;

                border:
                    2px dashed #E1A238;

                border-radius: 15px;

                padding:
                    15px 17px;

                margin-top: -6px;

                margin-bottom: 18px;
            ">

                <div style="
                    font-family:
                        'Space Grotesk',
                        sans-serif;

                    color: #A86408;

                    font-size: 13px;

                    font-weight: 700;

                    margin-bottom: 5px;
                ">
                    ✨ Pure AI Generation
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

                    color: #806126;

                    font-size: 14px;

                    line-height: 1.55;
                ">
                    No retrieved supporting source was found for this
                    statement. Treat it as a hypothesis or AI-generated
                    suggestion rather than a verified fact.
                </div>

            </div>
            """
        )


    # =====================================================
    # EVIDENCE
    # =====================================================

    with st.expander("📚 View Supporting Evidence"):

        if not evidence:

            st.info(
                "No supporting evidence was retrieved for this claim."
            )

        else:

            for index, source in enumerate(evidence):

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
                            ""
                        )
                    )
                )


                render_html(
                    f"""
                    <div style="
                        background: #FAFBFF;

                        border:
                            1px solid #E7E9F2;

                        border-radius: 15px;

                        padding:
                            16px;

                        margin-bottom: 12px;
                    ">

                        <div style="
                            font-family:
                                'Space Grotesk',
                                sans-serif;

                            color: #39415A;

                            font-size: 15px;

                            font-weight: 700;

                            margin-bottom: 8px;
                        ">
                            📖 {title}
                        </div>

                        <div style="
                            font-family:
                                'Quicksand',
                                sans-serif;

                            color: #697186;

                            font-size: 14px;

                            line-height: 1.6;
                        ">
                            {content}
                        </div>

                    </div>
                    """
                )


                if source.get("url"):

                    st.markdown(
                        f"[🔗 Read source →]({source['url']})"
                    )


                if index < len(evidence) - 1:

                    st.markdown("")


# =========================================================
# SUMMARY
# =========================================================

def display_summary(analyzed_claims):

    total = len(analyzed_claims)

    high = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper() == "HIGH"
    )

    medium = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper() == "MEDIUM"
    )

    speculative = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper() == "SPECULATIVE"
    )

    low = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper() == "LOW"
    )


    render_html(
        f"""
        <div style="
            margin-top: 30px;
            margin-bottom: 25px;
        ">

            <div style="
                font-family:
                    'Playfair Display',
                    serif;

                font-size: 29px;

                font-weight: 700;

                color: #20263A;

                margin-bottom: 15px;
            ">
                ✨ Trust Summary
            </div>


            <div style="
                display: grid;

                grid-template-columns:
                    repeat(5, 1fr);

                gap: 10px;
            ">


                <div style="
                    background: #FFFFFF;
                    border: 1px solid #E3E5EF;
                    border-radius: 16px;
                    padding: 15px;
                    text-align: center;
                ">
                    <div style="
                        font-family:
                            'Space Grotesk';
                        font-size: 25px;
                        font-weight: 700;
                        color: #7654E8;
                    ">
                        {total}
                    </div>

                    <div style="
                        font-family:
                            'Quicksand';
                        font-size: 12px;
                        color: #7A8195;
                    ">
                        Claims
                    </div>
                </div>


                <div style="
                    background: #F0FFF6;
                    border: 1px solid #D1F0DE;
                    border-radius: 16px;
                    padding: 15px;
                    text-align: center;
                ">
                    <div style="
                        font-family:
                            'Space Grotesk';
                        font-size: 25px;
                        font-weight: 700;
                        color: #168A4A;
                    ">
                        {high}
                    </div>

                    <div style="
                        font-family:
                            'Quicksand';
                        font-size: 12px;
                        color: #61806F;
                    ">
                        High
                    </div>
                </div>


                <div style="
                    background: #F0F7FF;
                    border: 1px solid #D7E8FA;
                    border-radius: 16px;
                    padding: 15px;
                    text-align: center;
                ">
                    <div style="
                        font-family:
                            'Space Grotesk';
                        font-size: 25px;
                        font-weight: 700;
                        color: #2874C7;
                    ">
                        {medium}
                    </div>

                    <div style="
                        font-family:
                            'Quicksand';
                        font-size: 12px;
                        color: #617B99;
                    ">
                        Medium
                    </div>
                </div>


                <div style="
                    background: #FFF8E8;
                    border: 1px solid #F2D89D;
                    border-radius: 16px;
                    padding: 15px;
                    text-align: center;
                ">
                    <div style="
                        font-family:
                            'Space Grotesk';
                        font-size: 25px;
                        font-weight: 700;
                        color: #A86408;
                    ">
                        {speculative}
                    </div>

                    <div style="
                        font-family:
                            'Quicksand';
                        font-size: 12px;
                        color: #8A6A35;
                    ">
                        Speculative
                    </div>
                </div>


                <div style="
                    background: #FFF2F2;
                    border: 1px solid #F0D3D3;
                    border-radius: 16px;
                    padding: 15px;
                    text-align: center;
                ">
                    <div style="
                        font-family:
                            'Space Grotesk';
                        font-size: 25px;
                        font-weight: 700;
                        color: #C83C3C;
                    ">
                        {low}
                    </div>

                    <div style="
                        font-family:
                            'Quicksand';
                        font-size: 12px;
                        color: #956565;
                    ">
                        Low
                    </div>
                </div>

            </div>

        </div>
        """
    )


# =========================================================
# ASK ANOTHER QUESTION
# =========================================================

def display_question_prompt():

    render_html(
        """
        <div style="
            text-align: center;

            margin-top: 48px;

            margin-bottom: 17px;

            padding-top: 30px;

            border-top:
                1px solid #E4E6F0;
        ">

            <div style="
                font-family:
                    'Playfair Display',
                    serif;

                font-size: 27px;

                font-weight: 700;

                color: #20263A;
            ">
                💭 Have another question?
            </div>

            <div style="
                font-family:
                    'Quicksand',
                    sans-serif;

                font-size: 14px;

                color: #7A8195;

                margin-top: 6px;
            ">
                Ask another question and discover how much you can trust
                the answer.
            </div>

        </div>
        """
    )
