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

    /* THE 'AHA' HERO BOX */
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
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    /* KINETIC BUTTONS */
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

    /* THE "SELECTED" STATE WITH VISUAL CHECKMARK */
    .stButton:has(div[data-testid="stMarkdown"] p:contains("SELECTED")) button {
        background-color: #00ADEF !important;
        color: #05101b !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.8) !important;
        font-weight: 800 !important;
    }

    /* Adding the checkmark via CSS pseudo-element */
    .stButton:has(div[data-testid="stMarkdown"] p:contains("SELECTED")) button::after {
        content: " ✓";
        font-size: 1.2rem;
        font-weight: 900;
    }

    .selection-marker { display: none !important; }
    
    .target-state {
        color: #00ADEF !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(0, 173, 239, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)
