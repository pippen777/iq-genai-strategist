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
    }

    /* UNIFIED MIDNIGHT GLASS INPUTS */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.03) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #00ADEF !important;
        box-shadow: 0 0 15px rgba(0, 173, 239, 0.3) !important;
    }

    /* KINETIC BUTTONS */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 65px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 600 !important; text-transform: uppercase !important;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important; transform: translateY(-3px) !important;
        box-shadow: 0 10px 25px rgba(0, 173, 239, 0.4) !important;
    }

    /* SELECTION LOCK */
    .stButton:has(p:contains("✓")) button {
        background-color: #00ADEF !important;
        background-image: none !important;
        color: #05101b !important; border: none !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.8) !important;
        transform: scale(1.02) !important; font-weight: 800 !important;
    }
    .stButton button p:contains("✓") { display: none !important; }

    /* IMPACT TABLE HIGHLIGHTS */
    .target-state {
        color: #00ADEF !important;
        font-weight: 800 !important;
        text-shadow: 0 0 10px rgba(0, 173, 239, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)
