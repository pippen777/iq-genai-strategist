import streamlit as st
from google import genai
import os

# 1. PAGE CONFIG & IQ BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important; color: white !important; }
    .title-text { background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem !important; font-weight: 800 !important; font-family: 'Arial Black', sans-serif !important; }
    
    /* Interactive Hover Buttons */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 75px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 0 15px 30px rgba(142, 45, 226, 0.4) !important;
        border: none !important;
    }
    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: white !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
def check_password():
    if st.query_params.get("wake") == "true":
        st.write("Engine Warm.")
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
    # 3. KNOWLEDGE LOADER
    def load_knowledge():
        try:
            with open("knowledge/iq_frameworks.txt", "r") as f: return f.read()
        except: return "IQ Business GESHIDO Philosophy: Value Weekly, Foundations Monthly."

    st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)
    
    # 4. STEP 1: MATURITY
    st.markdown('### Step 1: Diagnose Maturity')
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        if st.button("🔭 EXPLORER"): st.session_state.maturity = "Explorer"
    with m_col2:
        if st.button("🚀 SCALER"): st.session_state.maturity = "Scaler"
    with m_col3:
        if st.button("🤖 INNOVATOR"): st.session_state.maturity = "Innovator"

    # 5. STEP 2: INDUSTRY (SOUTH AFRICAN SECTOR BUTTONS)
    if "maturity" in st.session_state:
        st.markdown(f"**Diagnostic:** `{st.session_state.maturity}`")
        st.markdown('### Step 2: Select Industry Segment')
        
        # Grid of 5 buttons for top SA sectors
        i_col1, i_col2, i_col3, i_col4, i_col5 = st.columns(5)
        with i_col1:
            if st.button("🏦 Financial Services"): st.session_state.ind = "Financial Services"
        with i_col2:
            if st.button("🛒 Retail & FMCG"): st.session_state.ind = "Retail & FMCG"
        with i_col3:
            if st.button("📡 Telecoms"): st.session_state.ind = "Telecommunications"
        with i_col4:
            if st.button("🏛️ Public Sector"): st.session_state.ind = "Public Sector"
        with i_col5:
            if st.button("⛏️ Mining & Energy"): st.session_state.ind = "Mining & Energy"

    # 6. STEP 3: FRICTION & GENERATE
    if "ind" in st.session_state:
        st.markdown(f"**Industry Context:** `{st.session_state.ind}`")
        st.markdown('### Step 3: Define Friction Points')
        frictions = st.text_area("What are the top 3 friction points?", placeholder="e.g. Manual processing, data silos...")
        
        if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
            try:
                # Initialize client with key
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                
                # RESEARCH FIX: Using "gemini-1.5-flash" directly bypasses the v1beta prefixing bug
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=f"Strategist Context: {load_knowledge()}\n\nClient: {st.session_state.ind} ({st.session_state.maturity})\nFrictions: {frictions}\n\nTask: Generate a 12-week roadmap."
                )
                
                st.markdown("---")
                st.markdown(response.text)
                st.download_button("Download Strategy Brief", response.text, file_name="IQ_Strategy.md")

            except Exception as e:
                # If 1.5 still fails due to account era, auto-pivot to 2.0
                st.warning("Pivoting to GenAI 2.0 Engine...")
                try:
                    response = client.models.generate_content(model="gemini-2.0-flash", contents="...")
                    st.markdown(response.text)
                except:
                    st.error(f"Engine Error: {e}")
