import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background: #05070a !important; 
        background-image: radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.15) 0px, transparent 50%), 
                          radial-gradient(at 100% 100%, rgba(240, 47, 194, 0.15) 0px, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important; 
    }
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        font-size: 3.8rem !important; font-weight: 900 !important; letter-spacing: -2px;
    }
    div.stButton > button {
        background: rgba(255, 255, 255, 0.03) !important;
        color: rgba(255, 255, 255, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important; height: 65px !important; width: 100% !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-transform: uppercase; letter-spacing: 2px; font-weight: 600 !important;
    }
    div.stButton > button:hover {
        border-color: #00ADEF !important; color: #ffffff !important;
        background: rgba(0, 173, 239, 0.1) !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.4) !important; transform: translateY(-5px) !important;
    }
    .selected-btn div.stButton > button {
        background: linear-gradient(90deg, #00ADEF, #8E2DE2) !important;
        color: #ffffff !important; border: none !important; font-weight: 800 !important;
        box-shadow: 0 0 40px rgba(142, 45, 226, 0.6) !important;
    }
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); backdrop-filter: blur(20px);
        padding: 50px; border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center; margin: 40px 0;
    }
    .phase-card { 
        background: rgba(255, 255, 255, 0.01); padding: 40px; border-radius: 20px; 
        border-top: 4px solid #00ADEF; min-height: 450px;
    }
    .label-accent { color: #00ADEF; text-transform: uppercase; font-size: 0.75rem; font-weight: 800; letter-spacing: 4px; }
    </style>
    """, unsafe_allow_html=True)
