import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    /* 1. GLOBAL BACKGROUND FORCE */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #05070a !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.2) 0px, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(240, 47, 194, 0.2) 0px, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* 2. THE VISIONARY PINK GRADIENT TITLE */
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2) !important; 
        -webkit-background-clip: text !important; 
        -webkit-text-fill-color: transparent !important; 
        font-size: 4rem !important; 
        font-weight: 900 !important; 
        letter-spacing: -3px !important;
        filter: drop-shadow(0 0 15px rgba(240, 47, 194, 0.4)) !important; /* PINK GLOW */
    }

    /* 3. KINETIC BUTTONS: HOVER & GLOW */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important; 
        height: 65px !important; 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700 !important;
    }
    
    /* HOVER: IQ BLUE GLOW */
    div.stButton > button:hover {
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.2) !important;
        box-shadow: 0 0 35px rgba(0, 173, 239, 0.6) !important;
        transform: translateY(-5px) !important;
    }

    /* 4. SELECTION LOCK: THE NEON PINK-PURPLE GRADIENT */
    .selected-btn div.stButton > button {
        background: linear-gradient(90deg, #8E2DE2, #F02FC2) !important; /* PURPLE TO PINK */
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 0 45px rgba(240, 47, 194, 0.7) !important; /* PINK GLOW */
        transform: scale(1.05) !important;
    }

    /* 5. GLASS-IQ DASHBOARD */
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); 
        backdrop-filter: blur(25px);
        padding: 50px; border-radius: 20px; border: 1px solid rgba(240, 47, 194, 0.2); /* PINK TINT */
        text-align: center; margin: 40px 0;
    }
    
    .phase-card { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 35px; border-radius: 12px; 
        border-top: 4px solid #F02FC2 !important; /* FORCE PINK BORDER */
        min-height: 450px;
    }
    .phase-card:hover { 
        background: rgba(240, 47, 194, 0.05) !important; 
        box-shadow: 0 10px 30px rgba(240, 47, 194, 0.2) !important;
    }

    .label-accent { 
        color: #F02FC2 !important; /* PINK LABELS */
        text-transform: uppercase; 
        font-size: 0.8rem; font-weight: 800; letter-spacing: 4px; 
    }
    </style>
    """, unsafe_allow_html=True)
