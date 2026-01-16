import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;800&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    
    .stApp {
        background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* THE 'AHA' HERO BOX */
    .aha-box {
        padding: 45px;
        background: rgba(0, 173, 239, 0.08);
        border-left: 8px solid #00ADEF;
        border-radius: 20px;
        margin: 40px 0;
        box-shadow: 0 0 50px rgba(0, 173, 239, 0.15);
    }

    .aha-text {
        font-size: 2.4rem !important; /* THE CEO VIEW */
        font-weight: 800 !important;
        line-height: 1.2 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* THE TARGET IMPACT GLOW */
    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(0, 173, 239, 0.8);
    }

    .title-text {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important; font-weight: 800 !important;
    }

    /* PRIMARY KINETIC BUTTON */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        height: 65px !important;
        border-radius: 32px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(240, 47, 194, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }
    
    div.stButton > button[kind="primary"]:hover {
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 20px 40px rgba(240, 47, 194, 0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)
