import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important; color: white !important; }
    .title-text { background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem !important; font-weight: 800 !important; font-family: 'Arial Black', sans-serif !important; }
    
    /* 1. BASE BUTTON STYLE */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 75px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 600 !important;
    }

    /* 2. HOVER STYLE (The IQ Automation Glow) */
    div.stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 0 15px 30px rgba(142, 45, 226, 0.4) !important;
        color: white !important;
    }

    /* 3. SELECTED STATE (Same as Hover, but permanent) */
    .selected-btn div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(142, 45, 226, 0.5) !important;
        transform: scale(1.02) !important;
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
        pwd = st.text_input("Consultant Access Code", type="password", key="pwd_input")
        if st.button("Unlock GESHIDO® Engine"):
            if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Invalid Access Code.")
        return False
    return True

if check_password():
    st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)
    
    # STEP 1: MATURITY
    st.markdown('### Step 1: Diagnose Maturity')
    m_col1, m_col2, m_col3 = st.columns(3)
    
    maturity_options = {"Explorer": "🔭 EXPLORER", "Scaler": "🚀 SCALER", "Innovator": "🤖 INNOVATOR"}
    
    for i, (key, label) in enumerate(maturity_options.items()):
        with [m_col1, m_col2, m_col3][i]:
            if st.session_state.get("maturity") == key:
                st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
            if st.button(label, key=f"m_{key}"):
                st.session_state.maturity = key
                st.rerun()
            if st.session_state.get("maturity") == key:
                st.markdown('</div>', unsafe_allow_html=True)

    # STEP 2: INDUSTRY
    if "maturity" in st.session_state:
        st.markdown('### Step 2: Select Industry Segment')
        industries = {
            "Financial": "🏦 Financial Services",
            "Retail": "🛒 Retail & FMCG",
            "Telco": "📡 Telecoms",
            "Public": "🏛️ Public Sector",
            "Mining": "⛏️ Mining & Energy"
        }
        i_cols = st.columns(5)
        for i, (key, label) in enumerate(industries.items()):
            with i_cols[i]:
                if st.session_state.get("ind") == label:
                    st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
                if st.button(label, key=f"ind_{key}"): 
                    st.session_state.ind = label
                    st.rerun()
                if st.session_state.get("ind") == label:
                    st.markdown('</div>', unsafe_allow_html=True)

    # STEP 3: GENERATE
    if "ind" in st.session_state:
        st.markdown(f"**Strategy Path:** `{st.session_state.ind}` | `{st.session_state.maturity}`")
        frictions = st.text_area("Define top friction points:", placeholder="e.g. Inefficient loan processing...")
        
        if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
            try:
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(
                    f"Industry: {st.session_state.ind}, Maturity: {st.session_state.maturity}. Frictions: {frictions}. Create a 12-week GESHIDO roadmap."
                )
                st.markdown("---")
                st.markdown(response.text)
                st.download_button("Download Strategy Brief", response.text, file_name="IQ_Strategy.md")
            except Exception as e:
                st.error(f"Engine Error: {e}")
