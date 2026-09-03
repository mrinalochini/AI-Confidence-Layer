import html
import streamlit as st


# =========================================================
# HTML HELPER
# =========================================================

def render_html(content):
    """
    Safely render custom HTML using Streamlit's HTML renderer.
    This prevents HTML from appearing as code on the page.
    """
    st.html(content)


# =========================================================
# GLOBAL STYLE
# =========================================================

def load_css():

    render_html("""
    <style>

    /* =====================================================
       GOOGLE FONT IMPORTS
       ===================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap'
    );


    /* =====================================================
       PAGE BACKGROUND
       ===================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(126, 93, 255, 0.10),
                transparent 28%
            ),

            radial-gradient(
                circle at 90% 10%,
                rgba(50, 190, 220, 0.09),
                transparent 25%
            ),

            linear-gradient(
                135deg,
                #F7F8FF 0%,
                #F3F5FC 48%,
                #EEF3F8 100%
            );

    }


    /* =====================================================
       MAIN CONTENT WIDTH
       ===================================================== */

    .block-container {

        max-width: 980px !important;

        padding-top: 3rem !important;
        padding-bottom: 4rem !important;

    }


    /* =====================================================
       STREAMLIT DEFAULT TEXT
       ===================================================== */

    p, label {

        font-family:
            'DM Sans',
            sans-serif !important;

    }


    /* =====================================================
       QUESTION INPUT
       ===================================================== */

    div[data-testid="stTextInput"] input {

        background:
            #FFFFFF !important;

        color:
            #17213A !important;

        caret-color:
            #7357E8 !important;

        border:
            1.5px solid #D9DDEF !important;

        border-radius:
            16px !important;

        padding:
            15px 18px !important;

        font-family:
            'DM Sans',
            sans-serif !important;

        font-size:
            16px !important;

        font-weight:
            600 !important;

        box-shadow:
            0 7px 22px rgba(36, 48, 80, 0.06) !important;

        transition:
            all 0.2s ease !important;

    }


    div[data-testid="stTextInput"] input:focus {

        border:
            1.5px solid #7861E8 !important;

        box-shadow:
            0 0 0 4px rgba(120, 97, 232, 0.12),
            0 8px 24px rgba(36, 48, 80, 0.07) !important;

    }


    div[data-testid="stTextInput"] input::placeholder {

        color:
            #929AB0 !important;

        opacity:
            1 !important;

    }


    /* =====================================================
       ANALYZE BUTTON
       ===================================================== */

    div.stButton > button,
    div[data-testid="stFormSubmitButton"] button {

        background:
            linear-gradient(
                135deg,
                #7057E8,
                #4E82E8
            ) !important;

        color:
            #FFFFFF !important;

        border:
            none !important;

        border-radius:
            14px !important;

        padding:
            11px 23px !important;

        font-family:
            'Space Grotesk',
            sans-serif !important;

        font-size:
            14px !important;

        font-weight:
            700 !important;

        letter-spacing:
            0.2px !important;

        box-shadow:
            0 8px 20px rgba(94, 88, 210, 0.25) !important;

        transition:
            all 0.2s ease !important;

    }


    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] button:hover {

        transform:
            translateY(-2px) !important;

        box-shadow:
            0 12px 27px rgba(94, 88, 210, 0.34) !important;

    }


    div.stButton > button:active,
    div[data-testid="stFormSubmitButton"] button:active {

        transform:
            translateY(0px) !important;

    }


    /* =====================================================
       EXPANDERS
       ===================================================== */

    div[data-testid="stExpander"] {

        border:
            1px solid #E1E4F0 !important;

        border-radius:
            14px !important;

        background:
            rgba(255,255,255,0.78) !important;

        overflow:
            hidden !important;

    }


    div[data-testid="stExpander"] summary {

        font-family:
            'Space Grotesk',
            sans-serif !important;

        font-weight:
            600 !important;

        color:
            #35405C !important;

    }


    /* =====================================================
       WARNING / ERROR
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius:
            14px !important;

        font-family:
            'DM Sans',
            sans-serif !important;

    }


    </style>
    """)


# =========================================================
# HEADER
# =========================================================

def display_header():

    render_html("""
    <div style="
        margin-bottom:42px;

        padding:42px 35px 38px;

        text-align:center;

        background:
            linear-gradient(
                145deg,
                #FFFFFF 0%,
                #F5F2FF 55%,
                #EEF9FF 100%
            );

        border:
            1px solid #DEE2F0;

        border-radius:
            28px;

        box-shadow:
            0 18px 50px rgba(45, 55, 95, 0.09);

        position:relative;

        overflow:hidden;
    ">

        <!-- decorative glow -->

        <div style="
            position:absolute;
            width:180px;
            height:180px;
            border-radius:50%;
            background:#8D73F2;
            opacity:0.08;
            top:-90px;
            left:-50px;
        "></div>


        <div style="
            position:absolute;
            width:160px;
            height:160px;
            border-radius:50%;
            background:#42C7E8;
            opacity:0.07;
            bottom:-90px;
            right:-30px;
        "></div>


        <!-- brain -->

        <div style="
            font-size:45px;
            margin-bottom:12px;
        ">
            🧠
        </div>


        <!-- small technical label -->

        <div style="
            font-family:'Space Grotesk', sans-serif;
            font-size:10px;
            font-weight:700;
            letter-spacing:2.5px;
            color:#7666B9;
            text-transform:uppercase;
            margin-bottom:10px;
        ">
            INTELLIGENCE · EVIDENCE · TRUST
        </div>


        <!-- title -->

        <div style="
            font-family:'Space Grotesk', sans-serif;
            font-size:42px;
            line-height:1.12;
            font-weight:700;
            letter-spacing:-1.5px;
            color:#18233F;
        ">
            AI Confidence
            <span style="
                color:#7357E8;
            ">
                Layer
            </span>
        </div>


        <!-- subtitle -->

        <div style="
            margin-top:15px;

            font-family:'DM Sans', sans-serif;

            font-size:16px;

            line-height:1.7;

            color:#6E7890;
        ">
            Don't just get an AI answer.
            <br>

            <span style="
                color:#6248D8;
                font-weight:700;
            ">
                Understand why you should trust it.
            </span>
        </div>


        <!-- mini feature pills -->

        <div style="
            margin-top:23px;

            display:flex;

            justify-content:center;

            gap:8px;

            flex-wrap:wrap;
        ">

            <span style="
                padding:7px 12px;
                border-radius:999px;
                background:#F0EBFF;
                color:#654BD3;
                font-family:'Space Grotesk',sans-serif;
                font-size:11px;
                font-weight:600;
            ">
                ✦ CLAIM ANALYSIS
            </span>

            <span style="
                padding:7px 12px;
                border-radius:999px;
                background:#E8F8FC;
                color:#277F99;
                font-family:'Space Grotesk',sans-serif;
                font-size:11px;
                font-weight:600;
            ">
                ◈ EVIDENCE
            </span>

            <span style="
                padding:7px 12px;
                border-radius:999px;
                background:#FFF3D9;
                color:#9A6A19;
                font-family:'Space Grotesk',sans-serif;
                font-size:11px;
                font-weight:600;
            ">
                ◉ TRUST SIGNAL
            </span>

        </div>

    </div>
    """)


# =========================================================
# QUESTION PROMPT
# =========================================================

def display_question_prompt():

    render_html("""
    <div style="
        margin-top:58px;
        margin-bottom:18px;

        padding:31px 25px 27px;

        text-align:center;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F5F2FF 58%,
                #EEF9FF
            );

        border:
            1px solid #DFE2EF;

        border-radius:
            24px;

        box-shadow:
            0 12px 35px rgba(48, 57, 95, 0.07);
    ">

        <div style="
            font-size:28px;
            margin-bottom:7px;
        ">
            ✨
        </div>


        <div style="
            font-family:'Playfair Display', Georgia, serif;

            font-size:27px;

            font-weight:600;

            color:#26314D;
        ">
            What would you like to know next?
        </div>


        <div style="
            margin-top:8px;

            font-family:'DM Sans', sans-serif;

            font-size:14px;

            line-height:1.6;

            color:#7A849A;
        ">
            Ask something related to your previous question
            or explore a completely different topic.
        </div>


        <div style="
            margin-top:13px;

            font-family:'Space Grotesk', sans-serif;

            font-size:10px;

            font-weight:700;

            letter-spacing:1.4px;

            color:#9186B9;

            text-transform:uppercase;
        ">
            ✦ Keep exploring · Keep questioning AI
        </div>

    </div>
    """)


# =========================================================
# ANALYSIS HEADER
# =========================================================

def display_analysis_header():

    render_html("""
    <div style="
        margin-top:38px;
        margin-bottom:20px;

        display:flex;
        align-items:center;
        gap:12px;
    ">

        <div style="
            width:42px;
            height:42px;

            display:flex;
            align-items:center;
            justify-content:center;

            border-radius:13px;

            background:
                linear-gradient(
                    135deg,
                    #EDE7FF,
                    #E5F8FF
                );

            font-size:20px;
        ">
            ◈
        </div>


        <div>

            <div style="
                font-family:'Space Grotesk', sans-serif;

                font-size:10px;

                font-weight:700;

                letter-spacing:1.5px;

                color:#806BC3;

                text-transform:uppercase;
            ">
                TRUST ENGINE
            </div>


            <div style="
                font-family:'Space Grotesk', sans-serif;

                font-size:24px;

                font-weight:700;

                color:#25314C;
            ">
                Claim-by-Claim Analysis
            </div>

        </div>

    </div>
    """)


# =========================================================
# CLAIM DISPLAY
# =========================================================

def display_claim(claim, confidence, evidence):

    level = confidence.get(
        "confidence",
        "LOW"
    )

    reason = confidence.get(
        "reason",
        "There is not enough information to determine confidence."
    )


    # -----------------------------------------------------
    # ESCAPE USER / API CONTENT
    # -----------------------------------------------------

    safe_claim = html.escape(
        str(claim)
    )

    safe_reason = html.escape(
        str(reason)
    )


    # -----------------------------------------------------
    # COLORS / LABELS
    # -----------------------------------------------------

    if level == "HIGH":

        badge_background = "#E7F8EF"
        badge_text = "#218153"
        border_color = "#CBEADB"
        icon = "✓"
        label = "STRONGLY SUPPORTED"

    elif level == "MEDIUM":

        badge_background = "#FFF4DC"
        badge_text = "#9A6A16"
        border_color = "#F0D9A1"
        icon = "◐"
        label = "PARTIALLY SUPPORTED"

    else:

        badge_background = "#FFF1D9"
        badge_text = "#9A6515"
        border_color = "#E8C987"
        icon = "◇"
        label = "PURE GENERATION · SPECULATIVE"


    # -----------------------------------------------------
    # CLAIM CARD
    # -----------------------------------------------------

    render_html(f"""
    <div style="
        margin-bottom:24px;

        padding:25px 26px 23px;

        background:#FFFFFF;

        border:
            1px solid {border_color};

        border-radius:
            22px;

        box-shadow:
            0 10px 30px rgba(37, 47, 78, 0.065);

        position:relative;

        overflow:hidden;
    ">

        <!-- top accent -->

        <div style="
            position:absolute;

            top:0;
            left:0;
            right:0;

            height:4px;

            background:
                linear-gradient(
                    90deg,
                    #7658E8,
                    #54BDE0,
                    #E7B04C
                );
        "></div>


        <!-- claim header -->

        <div style="
            display:flex;

            align-items:center;

            justify-content:space-between;

            gap:12px;

            margin-bottom:17px;

            flex-wrap:wrap;
        ">


            <div style="
                font-family:'Space Grotesk', sans-serif;

                font-size:10px;

                font-weight:700;

                letter-spacing:1.4px;

                color:#8992A7;

                text-transform:uppercase;
            ">
                AI CLAIM
            </div>


            <div style="
                display:inline-flex;

                align-items:center;

                gap:6px;

                padding:7px 11px;

                border-radius:999px;

                background:{badge_background};

                color:{badge_text};

                font-family:'Space Grotesk', sans-serif;

                font-size:10px;

                font-weight:700;

                letter-spacing:.6px;
            ">
                {icon}
                {html.escape(label)}
            </div>

        </div>


        <!-- claim text -->

        <div style="
            font-family:'Manrope', sans-serif;

            font-size:18px;

            line-height:1.65;

            font-weight:600;

            color:#26314A;

            margin-bottom:20px;
        ">
            {safe_claim}
        </div>


        <!-- why -->

        <div style="
            padding:16px 18px;

            background:
                linear-gradient(
                    135deg,
                    #F7F5FF,
                    #F2FAFC
                );

            border-radius:15px;

            border:
                1px solid #E8E7F3;
        ">

            <div style="
                font-family:'Space Grotesk', sans-serif;

                font-size:10px;

                font-weight:700;

                letter-spacing:1.2px;

                color:#7968B3;

                text-transform:uppercase;

                margin-bottom:7px;
            ">
                WHY THIS RATING?
            </div>


            <div style="
                font-family:'DM Sans', sans-serif;

                font-size:14px;

                line-height:1.65;

                color:#657087;
            ">
                {safe_reason}
            </div>

        </div>

    </div>
    """)


    # =====================================================
    # SUPPORTING EVIDENCE
    # =====================================================

    with st.expander(
        "▸  View Supporting Evidence"
    ):

        if not evidence:

            render_html("""
            <div style="
                padding:18px;

                border-radius:14px;

                background:#FFF8E9;

                border:1px dashed #D9B96C;

                font-family:'DM Sans',sans-serif;

                color:#8A691F;

                font-size:14px;
            ">
                ◇ No retrieved source was found for this claim.
                This answer should therefore be treated as
                <b>pure generation / speculative</b>.
            </div>
            """)

        else:

            for index, source in enumerate(evidence):

                title = html.escape(
                    str(
                        source.get(
                            "title",
                            "Untitled source"
                        )
                    )
                )

                content = html.escape(
                    str(
                        source.get(
                            "content",
                            "No source content available."
                        )
                    )
                )

                url = html.escape(
                    str(
                        source.get(
                            "url",
                            "#"
                        )
                    )
                )


                render_html(f"""
                <div style="
                    margin-bottom:14px;

                    padding:17px 18px;

                    background:
                        linear-gradient(
                            135deg,
                            #F9FBFF,
                            #F3F8FC
                        );

                    border:
                        1px solid #DFE7EF;

                    border-radius:
                        15px;
                ">

                    <div style="
                        font-family:'Space Grotesk', sans-serif;

                        font-size:14px;

                        font-weight:700;

                        color:#263B59;

                        margin-bottom:8px;
                    ">
                        ◈ {title}
                    </div>


                    <div style="
                        font-family:'DM Sans', sans-serif;

                        font-size:13px;

                        line-height:1.65;

                        color:#6C788D;

                        margin-bottom:11px;
                    ">
                        {content}
                    </div>


                    <a
                        href="{url}"
                        target="_blank"
                        style="
                            font-family:'Space Grotesk', sans-serif;

                            font-size:11px;

                            font-weight:700;

                            color:#6652D6;

                            text-decoration:none;

                            letter-spacing:.4px;
                        "
                    >
                        OPEN SOURCE ↗
                    </a>

                </div>
                """)


# =========================================================
# SUMMARY
# =========================================================

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


    render_html(f"""
    <div style="
        margin-top:20px;
        margin-bottom:10px;
    ">

        <div style="
            font-family:'Space Grotesk', sans-serif;

            font-size:10px;

            font-weight:700;

            letter-spacing:1.5px;

            color:#8179A4;

            text-transform:uppercase;

            margin-bottom:12px;
        ">
            TRUST OVERVIEW
        </div>


        <div style="
            display:grid;

            grid-template-columns:
                repeat(4, 1fr);

            gap:10px;
        ">


            <!-- total -->

            <div style="
                padding:16px 12px;

                text-align:center;

                background:#FFFFFF;

                border:1px solid #E1E4EF;

                border-radius:16px;
            ">

                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:24px;

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


            <!-- high -->

            <div style="
                padding:16px 12px;

                text-align:center;

                background:#F0FAF5;

                border:1px solid #D5EDDF;

                border-radius:16px;
            ">

                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:24px;

                    font-weight:700;

                    color:#238153;
                ">
                    {high}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:10px;

                    font-weight:600;

                    color:#5E9278;
                ">
                    STRONG
                </div>

            </div>


            <!-- medium -->

            <div style="
                padding:16px 12px;

                text-align:center;

                background:#FFF8E9;

                border:1px solid #F0DFB4;

                border-radius:16px;
            ">

                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:24px;

                    font-weight:700;

                    color:#A1701C;
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


            <!-- low -->

            <div style="
                padding:16px 12px;

                text-align:center;

                background:#FFF4E3;

                border:1px dashed #DDBD75;

                border-radius:16px;
            ">

                <div style="
                    font-family:'Space Grotesk',sans-serif;

                    font-size:24px;

                    font-weight:700;

                    color:#9A681B;
                ">
                    {low}
                </div>

                <div style="
                    font-family:'DM Sans',sans-serif;

                    font-size:10px;

                    font-weight:600;

                    color:#9A7B3D;
                ">
                    SPECULATIVE
                </div>

            </div>

        </div>

    </div>
    """)
