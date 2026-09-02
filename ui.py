import html
import streamlit as st


# =========================================================
# HTML HELPER
# =========================================================

def render_html(content):
    """
    Use Streamlit's native HTML renderer.
    This prevents HTML from being displayed as code.
    """
    st.html(content)


# =========================================================
# PAGE CSS
# =========================================================

def load_css():

    st.html("""
    <style>

    /* =====================================================
       GOOGLE FONTS
       ===================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&family=Quicksand:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap'
    );


    /* =====================================================
       WHOLE PAGE
       ===================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(255, 210, 238, 0.55),
                transparent 27%
            ),

            radial-gradient(
                circle at 95% 10%,
                rgba(207, 227, 255, 0.65),
                transparent 30%
            ),

            radial-gradient(
                circle at 50% 100%,
                rgba(255, 231, 187, 0.45),
                transparent 35%
            ),

            #F8F9FF;

        color: #26324A;

    }


    /* =====================================================
       CONTENT WIDTH
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

        border: 2px solid #D9DDEF !important;

        border-radius: 17px !important;

        box-shadow:
            0 7px 22px rgba(67, 76, 120, 0.08) !important;

    }


    div[data-baseweb="input"]:hover {

        border-color: #B8B2EA !important;

    }


    div[data-baseweb="input"]:focus-within {

        background: #FFFFFF !important;

        border-color: #8064E8 !important;

        box-shadow:
            0 0 0 4px rgba(128, 100, 232, 0.12),
            0 8px 24px rgba(67, 76, 120, 0.10) !important;

    }


    /* THE ACTUAL TEXT THE USER TYPES */

    div[data-baseweb="input"] input {

        background: #FFFFFF !important;

        color: #20283D !important;

        -webkit-text-fill-color: #20283D !important;

        font-family:
            "DM Sans",
            sans-serif !important;

        font-size: 17px !important;

        font-weight: 500 !important;

    }


    /* PLACEHOLDER */

    div[data-baseweb="input"] input::placeholder {

        color: #969DB1 !important;

        -webkit-text-fill-color: #969DB1 !important;

        opacity: 1 !important;

    }


    /* =====================================================
       ENTER HINT
       ===================================================== */

    div[data-testid="InputInstructions"] {

        color: #9AA0B2 !important;

        font-family:
            "Quicksand",
            sans-serif !important;

    }


    /* =====================================================
       BUTTON
       ===================================================== */

    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {

        background:
            linear-gradient(
                135deg,
                #7756E8 0%,
                #A84FD3 50%,
                #4C91E9 100%
            ) !important;

        color: #FFFFFF !important;

        -webkit-text-fill-color: #FFFFFF !important;

        border: none !important;

        border-radius: 15px !important;

        min-height: 52px !important;

        padding: 10px 28px !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        box-shadow:
            0 9px 24px rgba(103, 78, 213, 0.25) !important;

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
                #6846DC,
                #963CC4,
                #3D82DC
            ) !important;

        color: #FFFFFF !important;

        transform: translateY(-2px);

        box-shadow:
            0 13px 30px rgba(103, 78, 213, 0.32) !important;

    }


    /* =====================================================
       EXPANDERS
       ===================================================== */

    div[data-testid="stExpander"] {

        background: #FFFFFF !important;

        border:
            1px solid #E0E4F0 !important;

        border-radius: 16px !important;

        margin-top: 12px !important;

        box-shadow:
            0 5px 18px rgba(65, 75, 120, 0.06) !important;

    }


    div[data-testid="stExpander"] summary {

        color: #414A63 !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-size: 14px !important;

        font-weight: 700 !important;

    }


    /* =====================================================
       WARNINGS / INFO
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 15px !important;

        font-family:
            "Quicksand",
            sans-serif !important;

    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {

        border-color: #E5E7F0 !important;

    }


    </style>
    """)


# =========================================================
# HEADER
# =========================================================

def display_header():

    render_html("""
    <div style="
        background:
            linear-gradient(
                135deg,
                #FFFFFF 0%,
                #FAF4FF 45%,
                #EFF8FF 100%
            );

        border: 1px solid #E2E2F0;

        border-radius: 28px;

        padding: 44px 35px;

        margin-bottom: 38px;

        text-align: center;

        box-shadow:
            0 15px 40px rgba(75, 84, 130, 0.10);
    ">

        <div style="
            font-size: 50px;
            margin-bottom: 12px;
        ">
            🧠✨
        </div>


        <div style="
            font-family:
                'Playfair Display',
                serif;

            font-size: 44px;

            font-weight: 700;

            color: #20283D;

            line-height: 1.15;

            margin-bottom: 16px;
        ">
            AI Confidence Layer
        </div>


        <div style="
            font-family:
                'Quicksand',
                sans-serif;

            font-size: 18px;

            color: #68728A;

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
    """)


# =========================================================
# ANALYSIS HEADER
# =========================================================

def display_analysis_header():

    render_html("""
    <div style="
        margin-top: 40px;
        margin-bottom: 20px;
    ">

        <div style="
            font-family:
                'Playfair Display',
                serif;

            font-size: 30px;

            font-weight: 700;

            color: #20283D;
        ">
            🔬 Claim-by-Claim Analysis
        </div>


        <div style="
            font-family:
                'Quicksand',
                sans-serif;

            font-size: 14px;

            color: #7B8499;

            margin-top: 6px;
        ">
            See exactly which parts of the answer deserve your trust.
        </div>

    </div>
    """)


# =========================================================
# CLAIM
# =========================================================

def display_claim(claim, confidence, evidence):

    level = str(
        confidence.get(
            "confidence",
            "LOW"
        )
    ).upper()


    reason = str(
        confidence.get(
            "reason",
            "No explanation was provided."
        )
    )


    safe_claim = html.escape(
        str(claim)
    )

    safe_reason = html.escape(
        reason
    )


    # =====================================================
    # HIGH
    # =====================================================

    if level == "HIGH":

        icon = "🟢"

        badge = "HIGH CONFIDENCE"

        badge_bg = "#E7F9EF"

        badge_color = "#168A4A"

        background = "#F5FFF9"

        border = "#CBEED9"

        label = "Evidence-backed claim"


    # =====================================================
    # MEDIUM
    # =====================================================

    elif level == "MEDIUM":

        icon = "🔵"

        badge = "MEDIUM CONFIDENCE"

        badge_bg = "#EAF3FF"

        badge_color = "#2874C7"

        background = "#F5FAFF"

        border = "#D1E5F8"

        label = "Partially supported claim"


    # =====================================================
    # SPECULATIVE
    # =====================================================

    elif level == "SPECULATIVE":

        icon = "✨"

        badge = "PURE GENERATION"

        badge_bg = "#FFF0C9"

        badge_color = "#A86408"

        background = "#FFF9EA"

        border = "#E7C36F"

        label = "AI-generated insight"


    # =====================================================
    # LOW
    # =====================================================

    else:

        icon = "🔴"

        badge = "LOW CONFIDENCE"

        badge_bg = "#FFEAEA"

        badge_color = "#C83C3C"

        background = "#FFF8F8"

        border = "#F0CCCC"

        label = "Weakly supported claim"


    # =====================================================
    # CLAIM CARD
    # =====================================================

    render_html(f"""
    <div style="
        background: {background};

        border:
            1px solid {border};

        border-radius: 23px;

        padding: 25px 27px;

        margin-bottom: 17px;

        box-shadow:
            0 9px 26px
            rgba(70, 76, 120, 0.07);
    ">

        <div style="
            display: flex;

            justify-content:
                space-between;

            align-items:
                center;

            gap: 15px;

            margin-bottom: 17px;
        ">

            <div style="
                font-family:
                    'Space Grotesk',
                    sans-serif;

                font-size: 12px;

                letter-spacing: 1.2px;

                text-transform: uppercase;

                color: #7A8195;

                font-weight: 700;
            ">
                {label}
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
                {icon} {badge}
            </div>

        </div>


        <div style="
            font-family:
                'DM Sans',
                sans-serif;

            font-size: 21px;

            line-height: 1.6;

            color: #26324A;

            font-weight: 600;
        ">
            {safe_claim}
        </div>


        <div style="
            margin-top: 21px;

            background:
                rgba(255,255,255,0.78);

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

                letter-spacing: 0.5px;

                margin-bottom: 5px;
            ">
                💡 WHY THIS RATING?
            </div>


            <div style="
                font-family:
                    'Quicksand',
                    sans-serif;

                color: #626B7E;

                font-size: 14px;

                line-height: 1.6;

                font-weight: 500;
            ">
                {safe_reason}
            </div>

        </div>

    </div>
    """)


    # =====================================================
    # SPECULATIVE NOTICE
    # =====================================================

    if level == "SPECULATIVE":

        render_html("""
        <div style="
            background: #FFF8E8;

            border:
                2px dashed #D89A2B;

            border-radius: 15px;

            padding:
                15px 17px;

            margin-top: -5px;

            margin-bottom: 17px;
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
                ✨ PURE AI GENERATION
            </div>


            <div style="
                font-family:
                    'Quicksand',
                    sans-serif;

                color: #806126;

                font-size: 14px;

                line-height: 1.55;
            ">
                No retrieved supporting source was found.
                Treat this statement as an AI-generated insight
                rather than a verified fact.
            </div>

        </div>
        """)


    # =====================================================
    # SUPPORTING EVIDENCE
    # =====================================================

    with st.expander("📚  View Supporting Evidence"):

        if not evidence:

            st.info(
                "No supporting evidence was retrieved for this claim."
            )

        else:

            for index, source in enumerate(evidence):

                source_title = html.escape(
                    str(
                        source.get(
                            "title",
                            "Source"
                        )
                    )
                )


                source_content = html.escape(
                    str(
                        source.get(
                            "content",
                            ""
                        )
                    )
                )


                render_html(f"""
                <div style="
                    background: #FAFBFF;

                    border:
                        1px solid #E4E7F0;

                    border-radius: 15px;

                    padding: 17px;

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
                        📖 {source_title}
                    </div>


                    <div style="
                        font-family:
                            'Quicksand',
                            sans-serif;

                        color: #697286;

                        font-size: 14px;

                        line-height: 1.6;
                    ">
                        {source_content}
                    </div>

                </div>
                """)


                if source.get("url"):

                    st.markdown(
                        f"[🔗 Read source →]({source['url']})"
                    )


# =========================================================
# TRUST SUMMARY
# =========================================================

def display_summary(analyzed_claims):

    total = len(analyzed_claims)


    high = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper()
        == "HIGH"
    )


    medium = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper()
        == "MEDIUM"
    )


    speculative = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper()
        == "SPECULATIVE"
    )


    low = sum(
        1
        for item in analyzed_claims
        if item["confidence"]["confidence"].upper()
        == "LOW"
    )


    render_html(f"""
    <div style="
        margin-top: 30px;
        margin-bottom: 25px;
    ">

        <div style="
            font-family:
                'Playfair Display',
                serif;

            font-size: 30px;

            font-weight: 700;

            color: #20283D;

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
                border: 1px solid #E2E5EF;
                border-radius: 16px;
                padding: 15px;
                text-align: center;
            ">

                <div style="
                    font-family:
                        'Space Grotesk',
                        sans-serif;

                    font-size: 25px;

                    font-weight: 700;

                    color: #7654E8;
                ">
                    {total}
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

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
                        'Space Grotesk',
                        sans-serif;

                    font-size: 25px;

                    font-weight: 700;

                    color: #168A4A;
                ">
                    {high}
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

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
                        'Space Grotesk',
                        sans-serif;

                    font-size: 25px;

                    font-weight: 700;

                    color: #2874C7;
                ">
                    {medium}
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

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
                        'Space Grotesk',
                        sans-serif;

                    font-size: 25px;

                    font-weight: 700;

                    color: #A86408;
                ">
                    {speculative}
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

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
                        'Space Grotesk',
                        sans-serif;

                    font-size: 25px;

                    font-weight: 700;

                    color: #C83C3C;
                ">
                    {low}
                </div>

                <div style="
                    font-family:
                        'Quicksand',
                        sans-serif;

                    font-size: 12px;

                    color: #956565;
                ">
                    Low
                </div>

            </div>

        </div>

    </div>
    """)


# =========================================================
# FOLLOW-UP QUESTION HEADER
# =========================================================

def display_question_prompt():

    render_html("""
    <div style="
        text-align: center;

        margin-top: 52px;

        margin-bottom: 20px;

        padding-top: 32px;

        border-top:
            1px solid #E1E4EF;
    ">

        <div style="
            font-family:
                'Playfair Display',
                serif;

            font-size: 28px;

            font-weight: 700;

            color: #20283D;
        ">
            💭 Have another question?
        </div>


        <div style="
            font-family:
                'Quicksand',
                sans-serif;

            font-size: 15px;

            color: #7A8195;

            margin-top: 7px;
        ">
            Ask something related to this answer —
            or explore something completely new.
        </div>

    </div>
    """)
