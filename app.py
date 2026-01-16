import streamlit as st
from google import genai
import os

# 1. PAGE CONFIG & BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important; color: white !important; }
    .title-text { background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem !important; font-weight: 800 !important; font-family: 'Arial Black', sans-serif !important; }
    .step-header { color: rgba(255, 255, 255, 0.6); text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem; margin-top: 30px; }
    
    /* Interactive Buttons - iqbusiness.net/automation style */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 70px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 600 !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 0 15px 30px rgba(142, 45, 226, 0.4) !important;
    }
    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: white !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE & WAKE-UP LOGIC
def check_password():
    if st.query_params.get("wake") == "true":
        st.write("GESHIDO Engine: Warm")
        st.stop()
    if "password_correct" not in st.session_state:
        st.markdown('<h1 class="title-text">Strategy Vault</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Consultant Access Code", type="password")
        if st.button("Unlock GESHIDO® Engine"):
            if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Invalid Access Code.")
        return False
    return True

if check_password():
    # 3. KNOWLEDGE BASE
    def load_knowledge():
        try:
            with open("knowledge/iq_frameworks.txt", "r") as f: return f.read()
        except: return "IQ Business GESHIDO Philosophy: Value Weekly, Foundations Monthly."

    st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)
    
    # 4. STEP 1: MATURITY
    st.markdown('<p class="step-header">Step 1: Diagnose Maturity</p>', unsafe_allow_html=True)
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        if st.button("🔭 EXPLORER"): st.session_state.maturity = "Explorer"
    with m_col2:
        if st.button("🚀 SCALER"): st.session_state.maturity = "Scaler"
    with m_col3:
        if st.button("🤖 INNOVATOR"): st.session_state.maturity = "Innovator"

    # 5. STEP 2: INDUSTRY (Buttons for SA Market)
    if "maturity" in st.session_state:
        st.markdown(f"**Diagnostic:** `{st.session_state.maturity}`")
        st.markdown('<p class="step-header">Step 2: Industry Segment</p>', unsafe_allow_html=True)
        i_col1, i_col2, i_col3, i_col4, i_col5 = st.columns(5)
        with i_col1:
            if st.button("🏦 Financial Services"): st.session_state.ind = "Financial Services"
        with i_col2:
            if st.button("🛒 Retail / FMCG"): st.session_state.ind = "Retail & FMCG"
        with i_col3:
            if st.button("📡 Telecoms"): st.session_state.ind = "Telecommunications"
        with i_col4:
            if st.button("🏛️ Public Sector"): st.session_state.ind = "Public Sector"
        with i_col5:
            if st.button("⛏️ Mining / Energy"): st.session_state.ind = "Mining & Energy"

    # 6. STEP 3: FRICTION & GENERATE
    if "ind" in st.session_state:
        st.markdown(f"**Context:** `{st.session_state.ind}`")
        st.markdown('<p class="step-header">Step 3: Define Friction Points</p>', unsafe_allow_html=True)
        frictions = st.text_area("What are the top 3 value pools or blockers?", placeholder="e.g. Manual claims processing, data silos...")
        
        if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
            try:
                # Use the stable SDK initialization
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                
                # RE-FIX: Standardize model name for the SDK
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=f"Context: {load_knowledge()}\n\nClient: {st.session_state.ind} ({st.session_state.maturity})\nFrictions: {frictions}\n\nTask: 12-week roadmap."
                )
                st.markdown("---")
                st.markdown(response.text)
                st.download_button("Download Strategy Brief", response.text, file_name="IQ_Strategy.md")
            except Exception as e:
                st.error(f"Engine Error: {e}")
