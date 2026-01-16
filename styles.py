import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    /* GLOBAL RESET & BACKGROUND */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #05070a !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.2) 0px, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(240, 47, 194, 0.2) 0px, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* THE GLOWING TITLE */
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2) !important; 
        -webkit-background-clip: text !important; 
        -webkit-text-fill-color: transparent !important; 
        font-size: 4rem !important; font-weight: 900 !important; letter-spacing: -3px !important;
        filter: drop-shadow(0 0 15px rgba(142, 45, 226, 0.5)) !important;
    }

    /* FORCING BUTTON STYLES */
    /* Target the base state */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important; 
        height: 60px !important; width: 100% !important;
        font-weight: 700 !important; text-transform: uppercase !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }
    
    /* Target the hover state specifically */
    .stButton > button:hover {
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.15) !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.5) !important;
        transform: translateY(-5px) !important;
        color: white !important;
    }

    /* TARGETING THE SELECTED STATE GRADIENT */
    /* This forces the Purple-to-Pink flip you loved */
    .selected-btn .stButton > button {
        background: linear-gradient(135deg, #8E2DE2, #F02FC2) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 0 40px rgba(240, 47, 194, 0.8) !important;
        transform: scale(1.05) !important;
    }

    /* LABELS & CARDS */
    .label-accent { 
        color: #00ADEF !important; 
        text-transform: uppercase; font-size: 0.8rem; font-weight: 800; letter-spacing: 4px; 
    }
    
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); backdrop-filter: blur(25px);
        padding: 50px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center; margin: 40px 0;
    }
    
    .phase-card { 
        background: rgba(255, 255, 255, 0.01); padding: 40px; border-radius: 15px; 
        border-top: 4px solid #00ADEF !important; min-height: 450px;
    }
    .phase-card:hover { border-top: 4px solid #F02FC2 !important; background: rgba(255, 255, 255, 0.03); }
    </style>
    """, unsafe_allow_html=True)
