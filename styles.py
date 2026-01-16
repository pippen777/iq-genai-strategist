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

    /* THE MASSIVE 'AHA' HERO */
    .aha-box {
        padding: 45px;
        background: rgba(0, 173, 239, 0.08);
        border-left: 8px solid #00ADEF;
        border-radius: 20px;
        margin: 40px 0;
        box-shadow: 0 0 50px rgba(0, 173, 239, 0.15);
    }

    .aha-text {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        line-height: 1.2 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* KINETIC BUTTONS (Idle/Hover) */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 65px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 15px 35px rgba(0, 173, 239, 0.4) !important;
        border: none !important;
    }

    /* THE SOLID BLUE LOCK */
    /* We target buttons inside a div that we will mark with 'selected-container' */
    div.selected-container .stButton > button {
        background-color: #00ADEF !important;
        background-image: none !important;
        color: #05101b !important;
        border: none !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.8) !important;
        font-weight: 800 !important;
        /* Visual checkmark */
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2305101b' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E") !important;
        background-repeat: no-repeat !important;
        background-position: right 15px center !important;
        padding-right: 40px !important;
    }

    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(0, 173, 239, 0.8);
    }
    
    /* THE ROADMAP BUTTON */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        height: 70px !important;
        border-radius: 35px !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
