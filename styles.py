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

    /* THE AWESOME ROADMAP BUTTON */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #8E2DE2, #F02FC2) !important;
        color: white !important;
        height: 70px !important;
        border-radius: 35px !important;
        border: none !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        letter-spacing: 2px !important;
        box-shadow: 0 10px 30px rgba(0, 173, 239, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        opacity: 1 !important; /* Forces it to be solid */
    }
    
    div.stButton > button[kind="primary"]:hover {
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 20px 45px rgba(240, 47, 194, 0.6) !important;
        color: white !important;
    }

    /* THE 'AHA' MOMENT HERO */
    .aha-box {
        padding: 50px;
        background: rgba(0, 173, 239, 0.08);
        border: 1px solid rgba(0, 173, 239, 0.2);
        border-radius: 25px;
        margin: 40px 0;
        text-align: center;
    }

    .aha-text {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* PHASE CARDS & TARGET GLOW */
    .phase-card {
        background: rgba(255, 255, 255, 0.05) !important;
        padding: 30px !important;
        border-radius: 20px !important;
        border-top: 5px solid #F02FC2 !important;
        margin-bottom: 25px !important;
    }
    
    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(0, 173, 239, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)
