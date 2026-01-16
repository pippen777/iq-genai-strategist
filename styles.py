import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* THE VISIONARY 'AHA' BOX */
    .aha-box {
        padding: 50px;
        background: rgba(0, 173, 239, 0.05);
        border: 1px solid rgba(0, 173, 239, 0.2);
        border-radius: 25px;
        margin: 40px 0;
        text-align: center;
        box-shadow: 0 0 60px rgba(0, 173, 239, 0.1);
    }

    .aha-text {
        font-size: 2.6rem !important; /* MASSIVE */
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* KINETIC PHASE CARDS */
    .phase-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px;
        border-radius: 20px;
        border-top: 5px solid #F02FC2;
        margin-bottom: 25px;
    }

    .phase-card h3 { color: #F02FC2 !important; font-size: 1.6rem !important; }

    /* TARGET ROI GLOW */
    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 20px rgba(0, 173, 239, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)
