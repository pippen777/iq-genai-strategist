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

    /* VISIONARY 'AHA' HERO */
    .aha-box {
        padding: 50px;
        background: rgba(0, 173, 239, 0.08);
        border: 1px solid rgba(0, 173, 239, 0.2);
        border-radius: 25px;
        margin: 40px 0;
        text-align: center;
        box-shadow: 0 0 60px rgba(0, 173, 239, 0.15);
    }

    .aha-text {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        line-height: 1.2 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* EXECUTIVE PHASE CARDS */
    .phase-card {
        background: rgba(255, 255, 255, 0.05) !important;
        padding: 30px !important;
        border-radius: 20px !important;
        border-top: 5px solid #F02FC2 !important;
        margin-bottom: 25px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
    }

    .phase-card h3 {
        color: #F02FC2 !important;
        margin-top: 0 !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
    }

    /* TARGET ROI GLOW */
    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(0, 173, 239, 0.8);
    }

    /* KINETIC BUTTONS */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        height: 60px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #F02FC2) !important;
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 15px 35px rgba(0, 173, 239, 0.4) !important;
        border: none !important;
    }

    /* SELECTION LOCK */
    .stButton button:has(p:contains("✓")) {
        background-color: #00ADEF !important;
        color: #0b101b !important;
        font-weight: 800 !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.8) !important;
    }
    </style>
    """, unsafe_allow_html=True)
