import html
import streamlit as st


# =========================================================
# HTML RENDERER
# =========================================================

def render_html(content):
    """
    Render custom HTML safely using Streamlit's HTML renderer.
    """
    st.html(content)


# =========================================================
# GLOBAL DESIGN
# =========================================================

def load_css():

    st.html("""
    <style>

    /* =====================================================
       FUTURISTIC FONT SYSTEM
       ===================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap'
    );


    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .stApp {

        background:

            radial-gradient(
                circle at 8% 5%,
                rgba(139, 92, 246, 0.12),
                transparent 25%
            ),

            radial-gradient(
                circle at 92% 8%,
                rgba(34, 211, 238, 0.12),
                transparent 25%
            ),

            radial-gradient(
                circle at 50% 100%,
                rgba(236, 72, 153, 0.08),
                transparent 30%
            ),

            linear-gradient(
                135deg,
                #F8FAFF 0%,
                #F9F7FF 50%,
                #F5FBFF 100%
            );

        color: #182238;

    }


    /* =====================================================
       CONTENT WIDTH
       ===================================================== */

    .block-container {

        max-width: 960px !important;

        padding-top: 2.5rem !important;

        padding-bottom: 5rem !important;

    }


    /* =====================================================
       REMOVE STREAMLIT DEFAULT TOP SPACE
       ===================================================== */

    header[data-testid="stHeader"] {

        background: transparent !important;

    }


    /* =====================================================
       QUESTION LABEL
       ===================================================== */

    .question-label {

        font-family:
            "Space Grotesk",
            sans-serif;

        font-size: 18px;

        font-weight: 700;

        color: #27324A;

        margin-bottom: 7px;

    }


    .question-description {

        font-family:
            "DM Sans",
            sans-serif;

        font-size: 14px;

        color: #778198;

        margin-bottom: 14px;

    }


    /* =====================================================
       TEXT INPUT
       ===================================================== */

    div[data-baseweb="input"] {

        background: rgba(255,255,255,0.94) !important;

        border: 1.5px solid #D9DDEF !important;

        border-radius: 18px !important;

        min-height: 58px !important;

        box-shadow:
            0 8px 28px rgba(70, 80, 130, 0.08) !important;

        transition:
            border-color .2s ease,
            box-shadow .2s ease !important;

    }


    div[data-baseweb="input"]:hover {

        border-color: #A99AEF !important;

    }


    div[data-baseweb="input"]:focus-within {

        background: #FFFFFF !important;

        border-color: #7657E8 !important;

        box-shadow:
            0 0 0 4px rgba(118,87,232,0.10),
            0 12px 32px rgba(91,76,180,0.12) !important;

    }


    /* ACTUAL TEXT USER TYPES */

    div[data-baseweb="input"] input {

        background: transparent !important;

        color: #172038 !important;

        -webkit-text-fill-color: #172038 !important;

        font-family:
            "DM Sans",
            sans-serif !important;

        font-size: 17px !important;

        font-weight: 600 !important;

    }


    div[data-baseweb="input"] input::placeholder {

        color: #9AA2B5 !important;

        -webkit-text-fill-color: #9AA2B5 !important;

        opacity: 1 !important;

    }


    /* =====================================================
       ENTER HINT
       ===================================================== */

    div[data-testid="InputInstructions"] {

        color: #9AA2B5 !important;

        font-family:
            "DM Sans",
            sans-serif !important;

    }


    /* =====================================================
       BUTTON
       ===================================================== */

    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {

        min-height: 52px !important;

        padding:
            9px 25px !important;

        border: none !important;

        border-radius: 15px !important;

        background:
            linear-gradient(
                135deg,
                #7657E8 0%,
                #9B5DE5 48%,
                #3AA8E8 100%
            ) !important;

        color: white !important;

        -webkit-text-fill-color: white !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-size: 15px !important;

        font-weight: 700 !important;

        letter-spacing: .2px !important;

        box-shadow:
            0 10px 26px
            rgba(107,82,215,0.25) !important;

        transition:
            transform .2s ease,
            box-shadow .2s ease !important;

    }


    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {

        transform:
            translateY(-2px) !important;

        box-shadow:
            0 14px 32px
            rgba(107,82,215,0.34) !important;

    }


    .stButton > button p,
    div[data-testid="stFormSubmitButton"] > button p {

        color: white !important;

        -webkit-text-fill-color: white !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-weight: 700 !important;

    }


    /* =====================================================
       EXPANDERS
       ===================================================== */

    div[data-testid="stExpander"] {

        background:
            rgba(255,255,255,0.78) !important;

        border:
            1px solid #E1E5F0 !important;

        border-radius: 17px !important;

        box-shadow:
            0 6px 22px
            rgba(63,73,110,0.06) !important;

        overflow: hidden !important;

    }


    div[data-testid="stExpander"] summary {

        color: #39435B !important;

        font-family:
            "Space Grotesk",
            sans-serif !important;

        font-size: 14px !important;

        font-weight: 700 !important;

    }


    /* =====================================================
       ALERTS
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 15px !important;

        font-family:
            "DM Sans",
            sans-serif !important;

    }


    </style>
    """)


# =========================================================
# HERO
# =========================================================

def display_header():

    render_html("""
    <div style="
        position:relative;
        overflow:hidden;

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,.97),
                rgba(248,246,255,.97)
            );

        border:1px solid rgba(215,218,238,.9);

        border-radius:30px;

        padding:42px 38px 39px;

        margin-bottom:36px;

        text-align:center;

        box-shadow:
            0 20px 50px
            rgba(68,75,125,.10);
    ">

        <!-- Decorative glow -->

        <div style="
            position:absolute;
            width:190px;
            height:190px;

            border-radius:50%;

            background:
                rgba(125,90,230,.10);

            filter:blur(45px);

            top:-80px;
            left:-60px;
        "></div>


        <div style="
            position:absolute;
            width:180px;
            height:180px;

            border-radius:50%;

            background:
                rgba(38,190,225,.10);

            filter:blur(45px);

            bottom:-90px;
            right:-50px;
        "></div>


        <!-- AI badge -->

        <div style="
            display:inline-flex;

            align-items:center;

            gap:7px;

            padding:
                7px 13px;

            border-radius:999px;

            background:
                linear-gradient(
                    135deg,
                    #F1ECFF,
                    #EAF8FF
                );

            border:
                1px solid #DDD9F3;

            color:#6953C8;

            font-family:
                'Space Grotesk',
                sans-serif;

            font-size:11px;

            font-weight:700;

            letter-spacing:1.3px;

            text-transform:uppercase;

            margin-bottom:17px;
        ">
            ✦ Evidence-Aware AI
        </div>


        <!-- Brain -->

        <div style="
            font-size:48px;

            line-height:1;

            margin-bottom:15px;
        ">
            🧠
        </div>


        <!-- Main title -->

        <div style="
            font-family:
                'Manrope',
                sans-serif;

            font-size:43px;

            font-weight:800;

            line-height:1.12;

            letter-spacing:-1.5px;

            background:
                linear-gradient(
                    90deg,
                    #26304A,
                    #704FE1,
                    #258FC8
                );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            margin-bottom:15px;
        ">
            AI Confidence Layer
        </div>


        <!-- Subtitle -->

        <div style="
            font-family:
                'DM Sans',
                sans-serif;

            font-size:17px;

            line-height:1.65;

            color:#707A91;

            max-width:650px;

            margin:auto;
        ">

            Don't just get an AI answer.

            <span style="
                color:#704FE1;

                font-weight:700;
            ">
                Understand why you should trust it.
            </span>

        </div>


        <!-- Small trust line -->

        <div style="
            margin-top:21px;

            font-family:
                'Space Grotesk',
                sans-serif;

            font-size:11px;

            color:#98A0B3;

            letter-spacing:.8px;

            text-transform:uppercase;
        ">
            Claims &nbsp;•&nbsp;
            Evidence &nbsp;•&nbsp;
            Confidence
        </div>

    </div>
    """)


# =========================================================
# ANALYSIS HEADER
# =========================================================

def display_analysis_header():

    render_html("""
    <div style="
        margin-top:42px;

        margin-bottom:21px;

        display:flex;

        align-items:center;

        gap:13px;
    ">

        <div style="
            width:43px;
            height:43px;

            border-radius:13px;

            display:flex;

            align-items:center;

            justify-content:center;

            background:
                linear-gradient(
                    135deg,
                    #EEE9FF,
                    #E7F8FF
                );

            border:
                1px solid #DDDDF0;

            font-size:20px;
        ">
            ✦
        </div>


        <div>

            <div style="
                font-family:
                    'Manrope',
                    sans-serif;

                font-size:28px;

                font-weight:800;

                color:#26304A;

                letter-spacing:-.6px;
            ">
                Claim-by-Claim Analysis
            </div>


            <div style="
                font-family:
                    'DM Sans',
                    sans-serif;

                font-size:13px;

                color:#8790A4;

                margin-top:3px;
            ">
                See what the AI said — and how strongly the evidence supports it.
            </div>

        </div>

    </div>
    """)


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

        icon = "✓"

        badge = "HIGH CONFIDENCE"

        accent = "#159A63"

        badge_bg = "#E7FAF2"

        card_bg = "#FBFFFD"

        border = "#CDEFE0"

        label = "Strongly supported"


    # =====================================================
    # MEDIUM
    # =====================================================

    elif level == "MEDIUM":

        icon = "◐"

        badge = "MEDIUM CONFIDENCE"

        accent = "#2587C8"

        badge_bg = "#E8F6FF"

        card_bg = "#FBFEFF"

        border = "#D2EAF8"

        label = "Partially supported"


    # =====================================================
    # SPECULATIVE
    # =====================================================

    elif level == "SPECULATIVE":

        icon = "✦"

        badge = "PURE GENERATION"

        accent = "#B77718"

        badge_bg = "#FFF2D2"

        card_bg = "#FFFCF4"

        border = "#E7CA88"

        label = "No retrieved source"


    # =====================================================
    # LOW
    # =====================================================

    else:

        icon = "!"

        badge = "LOW CONFIDENCE"

        accent = "#D45252"

        badge_bg = "#FFF0F0"

        card_bg = "#FFFBFB"

        border = "#F0D0D0"

        label = "Weakly supported"


    # =====================================================
    # MAIN CARD
    # =====================================================

    render_html(f"""
    <div style="
        position:relative;

        background:
            linear-gradient(
                135deg,
                {card_bg},
                #FFFFFF
            );

        border:
            1px solid {border};

        border-radius:23px;

        padding:26px 27px 24px;

        margin-bottom:16px;

        box-shadow:
            0 10px 30px
            rgba(60,72,110,.07);

        overflow:hidden;
    ">

        <!-- Accent line -->

        <div style="
            position:absolute;

            left:0;
            top:0;
            bottom:0;

            width:4px;

            background:{accent};
        "></div>


        <!-- Card header -->

        <div style="
            display:flex;

            justify-content:space-between;

            align-items:center;

            gap:15px;

            margin-bottom:18px;
        ">

            <div style="
                font-family:
                    'Space Grotesk',
                    sans-serif;

                font-size:11px;

                color:#8992A5;

                font-weight:700;

                letter-spacing:1.2px;

                text-transform:uppercase;
            ">
                {icon} &nbsp; {label}
            </div>


            <div style="
                display:inline-flex;

                align-items:center;

                gap:6px;

                background:{badge_bg};

                color:{accent};

                border-radius:999px;

                padding:8px 12px;

                font-family:
                    'Space Grotesk',
                    sans-serif;

                font-size:11px;

                font-weight:700;

                letter-spacing:.4px;

                white-space:nowrap;
            ">
                {badge}
            </div>

        </div>


        <!-- Claim -->

        <div style="
            font-family:
                'Manrope',
                sans-serif;

            font-size:20px;

            line-height:1.58;

            font-weight:650;

            color:#263149;
        ">
            {safe_claim}
        </div>


        <!-- Why -->

        <div style="
            margin-top:20px;

            padding:14px 16px;

            background:
                rgba(248,249,253,.82);

            border-radius:13px;

            border:
                1px solid #EAECF3;
        ">

            <div style="
                font-family:
                    'Space Grotesk',
                    sans-serif;

                font-size:10px;

                font-weight:700;

                color:{accent};

                letter-spacing:1px;

                margin-bottom:6px;

                text-transform:uppercase;
            ">
                Why this rating?
            </div>


            <div style="
                font-family:
                    'DM Sans',
                    sans-serif;

                font-size:14px;

                line-height:1.6;

                color:#697389;
            ">
                {safe_reason}
            </div>

        </div>

    </div>
    """)


    # =====================================================
    # PURE GENERATION NOTICE
    # =====================================================

    if level == "SPECULATIVE":

        render_html("""
        <div style="
            background:
                linear-gradient(
                    135deg,
                    #FFF9EA,
                    #FFFDF6
                );

            border:
                1.5px dashed #D5A13D;

            border-radius:16px;

            padding:15px 17px;

            margin-top:-4px;

            margin-bottom:17px;
        ">

            <div style="
                font-family:
                    'Space Grotesk',
                    sans-serif;

                font-size:11px;

                font-weight:700;

                color:#A86D13;

                letter-spacing:1px;

                margin-bottom:5px;
            ">
                ✦ PURE GENERATION · SPECULATIVE
            </div>


            <div style="
                font-family:
                    'DM Sans',
                    sans-serif;

                font-size:13px;

                line-height:1.6;

                color:#806A3C;
            ">
                No retrieved supporting source was found.
                Treat this as an AI-generated insight rather
                than a verified fact.
            </div>

        </div>
        """)


    # =====================================================
    # EVIDENCE
    # =====================================================

    with st.expander("▸  View Supporting Evidence"):

        if not evidence:

            st.info(
                "No supporting evidence was retrieved for this claim."
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
                            ""
                        )
                    )
                )


                render_html(f"""
                <div style="
                    background:#FBFCFF;

                    border:
                        1px solid #E4E7F1;

                    border-radius:15px;

                    padding:17px;

                    margin-bottom:12px;
                ">

                    <div style="
                        font-family:
                            'Space Grotesk',
                            sans-serif;

                        font-size:14px;

                        font-weight:700;

                        color:#39435B;

                        margin-bottom:7px;
                    ">
                        ◈ &nbsp; {title}
                    </div>


                    <div style="
                        font-family:
                            'DM Sans',
                            sans-serif;

                        font-size:13px;

                        line-height:1.65;

                        color:#6D778C;
                    ">
                        {content}
                    </div>

                </div>
                """)


                if source.get("url"):

                    st.markdown(
                        f"[↗ Open source]({source['url']})"
                    )


# =========================================================
# TRUST SUMMARY
# =========================================================

def display_summary(analyzed_claims):

    total = len(analyzed_claims)


    high = sum(
        1
        for item in analyzed_claims
        if str(
            item["confidence"]["confidence"]
        ).upper() == "HIGH"
    )


    medium = sum(
        1
        for item in analyzed_claims
        if str(
            item["confidence"]["confidence"]
        ).upper() == "MEDIUM"
    )


    speculative = sum(
        1
        for item in analyzed_claims
        if str(
            item["confidence"]["confidence"]
        ).upper() == "SPECULATIVE"
    )


    low = sum(
        1
        for item in analyzed_claims
        if str(
            item["confidence"]["confidence"]
        ).upper() == "LOW"
    )


    render_html(f"""
    <div style="
        margin-top:33px;

        margin-bottom:29px;

        background:
            rgba(255,255,255,.76);

        border:
            1px solid #E0E4F0;

        border-radius:22px;

        padding:22px;

        box-shadow:
            0 9px 28px
            rgba(64,74,115,.06);
    ">

        <div style="
            font-family:
                'Space Grotesk',
                sans-serif;

            font-size:11px;

            font-weight:700;

            letter-spacing:1.3px;

            color:#8A92A5;

            text-transform:uppercase;

            margin-bottom:6px;
        ">
            Overall assessment
        </div>


        <div style="
            font-family:
                'Manrope',
                sans-serif;

            font-size:25px;

            font-weight:800;

            color:#273149;

            margin-bottom:17px;
        ">
            ✦ Trust Summary
        </div>


        <div style="
            display:grid;

            grid-template-columns:
                repeat(5, 1fr);

            gap:9px;
        ">

            <div style="
                background:#F6F4FF;

                border:1px solid #E5E0FA;

                border-radius:14px;

                padding:13px 7px;

                text-align:center;
            ">
                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:23px;

                    font-weight:700;

                    color:#7657E8;
                ">
                    {total}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:11px;

                    color:#7F879A;
                ">
                    Claims
                </div>
            </div>


            <div style="
                background:#F0FCF7;

                border:1px solid #D8F1E5;

                border-radius:14px;

                padding:13px 7px;

                text-align:center;
            ">
                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:23px;

                    font-weight:700;

                    color:#159A63;
                ">
                    {high}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:11px;

                    color:#718D81;
                ">
                    High
                </div>
            </div>


            <div style="
                background:#F1FAFF;

                border:1px solid #D9EDF8;

                border-radius:14px;

                padding:13px 7px;

                text-align:center;
            ">
                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:23px;

                    font-weight:700;

                    color:#2587C8;
                ">
                    {medium}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:11px;

                    color:#71879A;
                ">
                    Medium
                </div>
            </div>


            <div style="
                background:#FFF9EA;

                border:1px solid #F0DCA8;

                border-radius:14px;

                padding:13px 7px;

                text-align:center;
            ">
                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:23px;

                    font-weight:700;

                    color:#B77718;
                ">
                    {speculative}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:11px;

                    color:#8B754E;
                ">
                    Pure Gen.
                </div>
            </div>


            <div style="
                background:#FFF4F4;

                border:1px solid #F1D7D7;

                border-radius:14px;

                padding:13px 7px;

                text-align:center;
            ">
                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:23px;

                    font-weight:700;

                    color:#D45252;
                ">
                    {low}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:11px;

                    color:#946D6D;
                ">
                    Low
                </div>
            </div>

        </div>

    </div>
    """)


# =========================================================
# FOLLOW-UP QUESTION
# =========================================================

def display_question_prompt():

    render_html("""
    <div style="
        position:relative;

        margin-top:58px;
        margin-bottom:18px;

        padding:30px 25px 25px;

        text-align:center;

        background:
            linear-gradient(
                135deg,
                rgba(246,243,255,.95),
                rgba(238,250,255,.95)
            );

        border:
            1px solid #DFE2F0;

        border-radius:24px;

        box-shadow:
            0 12px 35px
            rgba(73,78,125,.07);
    ">

        <div style="
            display:inline-flex;

            align-items:center;
            justify-content:center;

            width:43px;
            height:43px;

            border-radius:14px;

            background:
                linear-gradient(
                    135deg,
                    #EEE7FF,
                    #E4F8FF
                );

            font-size:21px;

            margin-bottom:10px;
        ">
            ✨
        </div>


        <div style="
            font-family:
                'Manrope',
                sans-serif;

            font-size:25px;

            font-weight:800;

            letter-spacing:-.4px;

            color:#29334C;
        ">
            What would you like to know next?
        </div>


        <div style="
            font-family:
                'DM Sans',
                sans-serif;

            font-size:14px;

            line-height:1.6;

            color:#7A8499;

            margin-top:7px;
        ">
            Ask something related to your previous question
            or explore a completely different topic.
        </div>


        <div style="
            margin-top:13px;

            font-family:
                'Space Grotesk',
                sans-serif;

            font-size:10px;

            font-weight:700;

            color:#9A91C4;

            letter-spacing:1px;

            text-transform:uppercase;
        ">
            ✦ Keep exploring · Keep questioning AI
        </div>

    </div>
    """)
