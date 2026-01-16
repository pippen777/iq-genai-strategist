import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    /* 1. OVERRIDE GLOBAL THEME */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #05070a !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.2) 0px, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(240, 47, 194, 0.2) 0px, transparent 50%) !important;
    }

    /* 2. HIDE DEFAULTS */
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }

    /* 3. TYPOGRAPHY */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    * { font-family: 'Outfit', sans-serif !important; color: white !important; }
    
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 4rem !important; font-weight: 900 !important; letter-spacing: -3px;
        margin-bottom: 20px;
    }

    /* 4. THE BUTTONS: FORCE HOVER & SELECTED */
    /* Target the button container specifically to fight Streamlit's internal CSS */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: rgba(255, 255, 255, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 4px !important;
        height: 65px !important;
        width: 100% !important;
        transition: all 0.3s ease-in-out !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
    }

    /* FORCE HOVER COLOR */
    .stButton > button:hover {
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.2) !important;
        box-shadow: 0 0 25px rgba(0, 173, 239, 0.5) !important;
        transform: translateY(-3px) !important;
        color: white !important;
    }

    /* FORCE SELECTED COLOR */
    .selected-btn .stButton > button {
        background: linear-gradient(90deg, #00ADEF, #8E2DE2) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 0 40px rgba(142, 45, 226, 0.7) !important;
        transform: scale(1.03) !important;
    }

    /* 5. DASHBOARD CARDS */
    .vision-container { 
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(25px);
        padding: 50px; border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center; margin: 40px 0; border-radius: 8px;
    }
    .phase-card { 
        background: rgba(255, 255, 255, 0.02); padding: 35px; border-radius: 8px;
        border-top: 4px solid #00ADEF; min-height: 420px;
    }
    .label-accent { color: #00ADEF; font-size: 0.75rem; font-weight: 800; letter-spacing: 4px; }
    </style>
    """, unsafe_allow_html=True)
