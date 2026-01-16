import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;800&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    
    /* RESTORED: Midnight Dark Background */
    .stApp {
        background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* RESTORED: Digital Integrator Gradient */
    .title-text {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
    }

    .step-header {
        color: rgba(255, 255, 255, 0.6);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        margin: 25px 0 10px 0;
    }

    /* RESTORED: THE "WOW" BUTTON */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 80px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 600 !important;
    }

    /* RESTORED: Kinetic Hover State */
    div.stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 0 15px 30px rgba(142, 45, 226, 0.4) !important;
        color: white !important;
    }

    /* RESTORED: Persistent Selection Glow */
    .selected-btn div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 0 40px rgba(0, 173, 239, 0.6) !important;
        transform: scale(1.03) !important;
    }

    /* RESTORED: Primary Action Button */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        height: 60px !important;
        border-radius: 30px !important;
        margin-top: 20px;
    }

    /* Glassmorphism Inputs */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)
