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

    /* 1. UNIVERSAL KINETIC HOVER (For Step 1 & 2 Buttons) */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 60px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid #00ADEF !important;
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0, 173, 239, 0.3) !important;
    }

    /* 2. THE SELECTED STATE (Solid Blue Lock) */
    .stButton button:has(p:contains("✓")) {
        background-color: #00ADEF !important;
        color: #0b101b !important;
        border: none !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.6) !important;
        transform: scale(1.02) !important;
    }

    /* 3. THE HERO ROADMAP BUTTON (Solid Gradient) */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #8E2DE2, #F02FC2) !important;
        color: white !important;
        height: 70px !important;
        border-radius: 35px !important;
        border: none !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        letter-spacing: 2px !important;
        box-shadow: 0 10px 30px rgba(0, 173, 239, 0.4) !important;
        margin-top: 20px !important;
    }
    
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 20px 45px rgba(240, 47, 194, 0.6) !important;
    }

    /* 4. STRATEGIC OUTPUT CLASSES */
    .aha-box {
        padding: 45px;
        background: rgba(0, 173, 239, 0.08);
        border-left: 8px solid #00ADEF;
        border-radius: 20px;
        margin: 40px 0;
    }
    .aha-text {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .phase-card {
        background: rgba(255, 255, 255, 0.05) !important;
        padding: 25px !important;
        border-radius: 15px !important;
        border-top: 4px solid #F02FC2 !important;
        margin-bottom: 20px !important;
    }
    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(0, 173, 239, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)
