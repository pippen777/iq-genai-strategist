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
        transition: all 0.3s ease !important;
    }

    /* HOVER STYLE */
    div.stButton > button:hover {
        border: 1px solid #00ADEF !important;
        background: rgba(0, 173, 239, 0.1) !important;
    }

    /* SELECTED STATE - KEEP THE GLOW */
    .selected-btn div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(142, 45, 226, 0.6) !important;
        color: white !important;
    }

    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">Strategy Vault</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Access Code", type="password")
    if st.button("Unlock"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

# 3. KNOWLEDGE
def load_knowledge():
    try:
        with open("knowledge/iq_frameworks.txt", "r") as f: return f.read()
    except: return "IQ GESHIDO: Value Weekly, Foundations Monthly."

st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)

# 4. STEP 1: MATURITY
st.markdown('### Step 1: Diagnose Maturity')
m_cols = st.columns(3)
opts = {"Explorer": "🔭 EXPLORER", "Scaler": "🚀 SCALER", "Innovator": "🤖 INNOVATOR"}

for i, (k, v) in enumerate(opts.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k:
            st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button(v, key=f"m_{k}"):
            st.session_state.maturity = k
            st.rerun()
        if st.session_state.get("maturity") == k:
            st.markdown('</div>', unsafe_allow_html=True)

# 5. STEP 2: INDUSTRY
if "maturity" in st.session_state:
    st.markdown('### Step 2: Select Industry Segment')
    i_cols = st.columns(5)
    inds = {"Fin": "🏦 Financial", "Ret": "🛒 Retail", "Tel": "📡 Telecoms", "Pub": "🏛️ Public", "Min": "⛏️ Mining"}
    for i, (k, v) in enumerate(inds.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v:
                st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
            if st.button(v, key=f"i_{k}"):
                st.session_state.ind = v
                st.rerun()
            if st.session_state.get("ind") == v:
                st.markdown('</div>', unsafe_allow_html=True)

# 6. STEP 3: GENERATE
if "ind" in st.session_state:
    st.markdown(f"**Path Locked:** `{st.session_state.ind}` | `{st.session_state.maturity}`")
    frictions = st.text_area("Friction Points:", placeholder="Define the blockers...")
    
    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
        try:
            # LEGACY CONFIGURATION (Most stable)
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            response = model.generate_content(
                f"Context: {load_knowledge()}\nIndustry: {st.session_state.ind}\nMaturity: {st.session_state.maturity}\nFrictions: {frictions}\nTask: 12-week GESHIDO roadmap."
            )
            st.markdown("---")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Engine Error: {e}")
