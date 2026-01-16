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

    /* THE 'FORCE-HOVER' SELECTOR */
    /* We target the button and its internal paragraph to ensure the color sticks */
    div[data-testid="stButton"] button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2) !important;
        border: 1px solid #F02FC2 !important;
        transform: scale(1.05) translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0, 173, 239, 0.4) !important;
    }
    
    div[data-testid="stButton"] button:hover p {
        color: white !important;
    }
/* Update your .title-text class in styles.py */
.title-text {
    font-size: 56px !important;
    font-weight: 800 !important;
    background: linear-gradient(90deg, #00ADEF 0%, #F02FC2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 10px 30px rgba(0, 173, 239, 0.3);
    letter-spacing: -1px;
    margin-bottom: 40px !important;
}
    /* UNIVERSAL BUTTON BASE */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 60px !important;
        width: 100% !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    /* THE SOLID BLUE LOCK */
    .stButton button:has(p:contains("✓")) {
        background-color: #00ADEF !important;
        background-image: none !important;
        color: #05101b !important;
        border: none !important;
        box-shadow: 0 0 30px rgba(0, 173, 239, 0.8) !important;
    }
    
    .stButton button:has(p:contains("✓")) p {
        color: #05101b !important;
        font-weight: 800 !important;
    }

    /* THE PRIMARY ROADMAP BUTTON */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #00ADEF, #8E2DE2, #F02FC2) !important;
        height: 70px !important;
        border-radius: 35px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(0, 173, 239, 0.4) !important;
    }
/* Add this inside the <style> tag in styles.py */
.blindspot-card {
    background: rgba(240, 47, 194, 0.05) !important;
    border: 1px solid #F02FC2 !important;
    padding: 20px !important;
    border-radius: 12px !important;
    margin: 20px 0 !important;
    color: #FFFFFF !important;
}

.aha-box h3 {
    color: #00ADEF !important;
    margin-top: 0 !important;
}
    /* OUTPUT STYLING */
    .aha-box { padding: 40px; background: rgba(0, 173, 239, 0.08); border-left: 8px solid #00ADEF; border-radius: 20px; margin: 30px 0; }
    .aha-text { font-size: 2.2rem !important; font-weight: 800; background: linear-gradient(90deg, #00ADEF, #FFFFFF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .phase-card { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; border-top: 4px solid #F02FC2; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)
