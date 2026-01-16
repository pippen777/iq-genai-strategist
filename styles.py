import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background: #05070a !important; 
        background-image: radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.12) 0, transparent 50%), 
                          radial-gradient(at 100% 100%, rgba(142, 45, 226, 0.12) 0, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important; 
    }
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        font-size: 3.5rem !important; font-weight: 900 !important; letter-spacing: -2px;
    }
    /* BUTTON HOVER & SELECTION */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 4px !important; height: 60px !important; width: 100% !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem !important;
    }
    div.stButton > button:hover {
        background: rgba(0, 173, 239, 0.15) !important;
        color: #ffffff !important; border: 1px solid #00ADEF !important;
        box-shadow: 0 0 25px rgba(0, 173, 239, 0.4) !important; transform: translateY(-2px);
    }
    .selected-btn div.stButton > button {
        background: linear-gradient(90deg, #00ADEF, #8E2DE2) !important;
        color: #ffffff !important; border: none !important; font-weight: 700 !important;
        box-shadow: 0 0 40px rgba(142, 45, 226, 0.6) !important;
    }
    /* DASHBOARD CARDS */
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); backdrop-filter: blur(20px);
        padding: 50px; border: 1px solid rgba(255, 255, 255, 0.05); text-align: center; margin: 30px 0;
    }
    .phase-card { 
        background: rgba(255, 255, 255, 0.01); padding: 30px; border-left: 3px solid #00ADEF; min-height: 400px;
    }
    .label-accent { color: #00ADEF; text-transform: uppercase; font-size: 0.7rem; font-weight: 700; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)
