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

    /* THE 10/10 IDLE BUTTON */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 70px !important; width: 100% !important;
        transition: all 0.3s ease !important;
        font-weight: 600 !important; text-transform: uppercase !important;
    }

    /* THE BEAUTIFUL HOVER */
    .stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 25px rgba(0, 173, 239, 0.4) !important;
    }

    /* THE SURGICAL STRIKE: SOLID BLUE LOCK */
    /* This targets buttons that are specifically marked as 'active' via a hack */
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stMarkdown"] p:contains("ACTIVE_SELECTION")) + div .stButton button {
        background-color: #00ADEF !important;
        background-image: none !important;
        color: #05070a !important;
        border: none !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.8) !important;
        font-weight: 800 !important;
    }
    
    /* Hiding the logic marker */
    .selection-marker { display: none !important; }
    </style>
    """, unsafe_allow_html=True)
