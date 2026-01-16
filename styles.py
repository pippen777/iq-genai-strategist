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

    .title-text {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important; font-weight: 800 !important;
        margin-bottom: 0px;
    }

    .step-header {
        color: rgba(255, 255, 255, 0.6);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        margin: 25px 0 10px 0;
    }

    /* THE 'AHA' MOMENT BOX */
    .aha-box {
        padding: 40px;
        background: rgba(0, 173, 239, 0.08);
        border-left: 8px solid #00ADEF;
        border-radius: 20px;
        margin: 30px 0;
        box-shadow: 0 0 50px rgba(0, 173, 239, 0.1);
    }

    .aha-text {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        line-height: 1.2 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    /* THE EXECUTIVE PHASE CARDS */
    .phase-card {
        background: rgba(255, 255, 255, 0.05) !important;
        padding: 25px !important;
        border-radius: 15px !important;
        border-top: 4px solid #F02FC2 !important;
        margin-bottom: 20px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    }

    .phase-card h3 {
        color: #F02FC2 !important;
        margin-top: 0 !important;
        font-size: 1.4rem !important;
    }

    /* BUTTONS & SELECTION */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 60px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        transform: scale(1.03) translateY(-3px) !important;
        border: none !important;
    }

    .stButton button:has(p:contains("✓")) {
        background-color: #00ADEF !important;
        color: #05101b !important;
        border: none !important;
        box-shadow: 0 0 25px rgba(0, 173, 239, 0.5) !important;
        font-weight: 800 !important;
    }

    .target-state {
        color: #00ADEF !important;
        font-weight: 800 !important;
        text-shadow: 0 0 10px rgba(0, 173, 239, 0.5);
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        height: 65px !important;
        border-radius: 32px !important;
        font-weight: 800 !important;
    }
    </style>
    """, unsafe_allow_html=True)
