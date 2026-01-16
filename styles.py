import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    /* 1. FORCE THE LIQUID SPACE BACKGROUND */
    html, body, [data-testid="stAppViewContainer"] {
        background: #05070a !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.15) 0px, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(240, 47, 194, 0.15) 0px, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* 2. THE VISIONARY TITLE */
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 4rem !important; 
        font-weight: 900 !important; 
        letter-spacing: -3px;
        filter: drop-shadow(0 0 15px rgba(142, 45, 226, 0.4));
    }

    /* 3. KINETIC BUTTONS: HOVER & GLOW */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.04) !important;
        color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important; 
        height: 65px !important; 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700 !important;
    }
    
    div.stButton > button:hover {
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.15) !important;
        box-shadow: 0 0 35px rgba(0, 173, 239, 0.5) !important;
        transform: translateY(-5px) scale(1.03) !important;
        color: #fff !important;
    }

    /* 4. SELECTION LOCK: THE NEON GRADIENT */
    .selected-btn div.stButton > button {
        background: linear-gradient(90deg, #00ADEF, #8E2DE2) !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 0 45px rgba(142, 45, 226, 0.7) !important;
        transform: scale(1.05) !important;
    }

    /* 5. GLASS-IQ DASHBOARD */
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); 
        backdrop-filter: blur(25px);
        padding: 60px; border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center; margin: 40px 0;
    }
    
    .phase-card { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 40px; border-radius: 20px; 
        border-top: 4px solid #00ADEF;
        min-height: 450px;
        transition: all 0.3s ease;
    }
    .phase-card:hover { border-top: 4px solid #F02FC2; background: rgba(255, 255, 255, 0.04); }

    .label-accent { 
        color: #00ADEF; text-transform: uppercase; 
        font-size: 0.8rem; font-weight: 800; letter-spacing: 4px; 
    }
    </style>
    """, unsafe_allow_html=True)
