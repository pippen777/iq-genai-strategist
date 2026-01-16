import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    # Target specific button keys using Streamlit's internal 'st-key' prefix
    st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none !important; }}
    .stApp {{ background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important; color: white !important; }}
    .title-text {{ background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem !important; font-weight: 800 !important; font-family: 'Arial Black', sans-serif !important; }}
    
    /* UNIVERSAL BUTTON STYLE */
    div.stButton > button {{
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 75px !important;
        transition: all 0.4s ease !important;
    }}

    /* HOVER GLOW */
    div.stButton > button:hover {{
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(142, 45, 226, 0.5) !important;
        transform: translateY(-3px) !important;
    }}

    /* SELECTED STATE: Force the active button to keep the glow */
    div[data-testid="stButton"] button[aria-pressed="true"], 
    .selected-glow div.stButton > button {{
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(142, 45, 226, 0.7) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">Strategy Vault</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Access Code", type="password")
    if st.button("Unlock GESHIDO® Engine"):
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
        # Wrap the button in a div that applies the 'selected-glow' if selected
        is_selected = st.session_state.get("maturity") == k
        if is_selected: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
        if st.button(v, key=f"mat_{k}"):
            st.session_state.maturity = k
            st.rerun()
        if is_selected: st.markdown('</div>', unsafe_allow_html=True)

# 5. STEP 2: INDUSTRY
if "maturity" in st.session_state:
    st.markdown('### Step 2: Select Industry Segment')
    i_cols = st.columns(5)
    inds = {"Fin": "🏦 Financial", "Ret": "🛒 Retail", "Tel": "📡 Telecoms", "Pub": "🏛️ Public", "Min": "⛏️ Mining"}
    for i, (k, v) in enumerate(inds.items()):
        with i_cols[i]:
            is_selected = st.session_state.get("ind") == v
            if is_selected: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"):
                st.session_state.ind = v
                st.rerun()
            if is_selected: st.markdown('</div>', unsafe_allow_html=True)

# 6. STEP 3: GENERATE (FORCED V1 STABLE)
if "ind" in st.session_state:
    st.markdown(f"**Path Locked:** `{st.session_state.ind}` | `{st.session_state.maturity}`")
    frictions = st.text_area("Friction Points:", placeholder="Define the blockers...")
    
    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
        try:
            # FIX: Configure to use stable Gemini 1.5 Flash
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            
            # Use 'gemini-1.5-flash' - research shows this is the most stable alias
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            response = model.generate_content(
                f"Context: {load_knowledge()}\nIndustry: {st.session_state.ind}\nMaturity: {st.session_state.maturity}\nFrictions: {frictions}\nTask: 12-week roadmap."
            )
            st.markdown("---")
            st.markdown(response.text)
        except Exception as e:
            # Fallback to gemini-pro if Flash remains region-locked
            st.error(f"Primary Engine Restricted. Attempting Legacy Fallback...")
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content("...")
                st.markdown(response.text)
            except:
                st.error(f"Final Engine Error: {e}")
