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
    
    /* BASE BUTTON STYLE */
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

    /* HOVER STYLE (The IQ Automation Glow) */
    div.stButton > button:hover {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 30px rgba(142, 45, 226, 0.4) !important;
    }

    /* SELECTED STATE: Keeps the glow locked in */
    .st-emotion-cache-1v07p6k e1nzilvr4, /* Specific Streamlit button target */
    .selected-btn div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(142, 45, 226, 0.6) !important;
    }

    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: white !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
def check_password():
    if st.query_params.get("wake") == "true":
        st.write("Uptime Monitor Active: Engine Warm.")
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
    st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)
    
    # --- STEP 1: MATURITY ---
    st.markdown('### Step 1: Diagnose Maturity')
    m_cols = st.columns(3)
    maturity_map = {"Explorer": "🔭 EXPLORER", "Scaler": "🚀 SCALER", "Innovator": "🤖 INNOVATOR"}
    
    for i, (m_key, m_label) in enumerate(maturity_map.items()):
        with m_cols[i]:
            if st.session_state.get("maturity") == m_key:
                st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
            if st.button(m_label, key=f"m_{m_key}"):
                st.session_state.maturity = m_key
                st.rerun()
            if st.session_state.get("maturity") == m_key:
                st.markdown('</div>', unsafe_allow_html=True)

    # --- STEP 2: INDUSTRY ---
    if "maturity" in st.session_state:
        st.markdown('### Step 2: Select Industry Segment')
        i_cols = st.columns(5)
        ind_map = {
            "Fin": "🏦 Financial Services",
            "Ret": "🛒 Retail & FMCG",
            "Tel": "📡 Telecoms",
            "Pub": "🏛️ Public Sector",
            "Min": "⛏️ Mining & Energy"
        }
        for i, (i_key, i_label) in enumerate(ind_map.items()):
            with i_cols[i]:
                if st.session_state.get("ind") == i_label:
                    st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
                if st.button(i_label, key=f"i_{i_key}"):
                    st.session_state.ind = i_label
                    st.rerun()
                if st.session_state.get("ind") == i_label:
                    st.markdown('</div>', unsafe_allow_html=True)

    # --- STEP 3: GENERATE ---
    if "ind" in st.session_state:
        st.markdown(f"**Path Locked:** `{st.session_state.ind}` | `{st.session_state.maturity}`")
        frictions = st.text_area("Define top friction points:", placeholder="e.g. Inefficient loan processing...")
        
        if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
            try:
                # RESEARCH FIX: Force the V1 endpoint to bypass the 404 NOT_FOUND
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                
                # We use the GenerativeModel call directly to avoid the beta pathing
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                response = model.generate_content(
                    f"IQ Strategist Prompt: Industry {st.session_state.ind}, Maturity {st.session_state.maturity}. Frictions: {frictions}. Create a GESHIDO roadmap."
                )
                st.markdown("---")
                st.markdown(response.text)
                st.download_button("Download Strategy Brief", response.text, file_name="IQ_Strategy.md")
            except Exception as e:
                st.error(f"Engine Error: {e}")
