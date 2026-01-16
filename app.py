import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & EXECUTIVE BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important; color: white !important; }
    .title-text { background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem !important; font-weight: 800 !important; font-family: 'Arial Black', sans-serif !important; }
    
    /* Executive Dashboard Components */
    .vision-header {
        background: linear-gradient(90deg, rgba(0,173,239,0.15) 0%, rgba(240,47,194,0.15) 100%);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(0, 173, 239, 0.5);
        text-align: center;
        margin: 20px 0 40px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .exec-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        height: 100%;
        border-top: 4px solid #8E2DE2;
    }
    .metric-box {
        background: rgba(0, 173, 239, 0.1);
        border: 1px dashed #00ADEF;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }

    /* Interactive Buttons */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 70px !important;
        transition: all 0.4s ease !important;
    }
    div.stButton > button:hover, .selected-glow div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(142, 45, 226, 0.6) !important;
        transform: translateY(-3px) !important;
    }
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

# 3. KNOWLEDGE LOADER
def load_knowledge():
    try:
        with open("knowledge/iq_frameworks.txt", "r") as f: return f.read()
    except: return "IQ Business GESHIDO Strategy: Value Weekly, Foundations Monthly."

st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)

# 4. STEP 1 & 2: INPUTS
col_m1, col_m2 = st.columns([1, 1])
with col_m1:
    st.markdown('### Step 1: Diagnose Maturity')
    m_cols = st.columns(3)
    opts = {"Explorer": "🔭 EXPLORER", "Scaler": "🚀 SCALER", "Innovator": "🤖 INNOVATOR"}
    for i, (k, v) in enumerate(opts.items()):
        with m_cols[i]:
            if st.session_state.get("maturity") == k: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"m_{k}"): st.session_state.maturity = k; st.rerun()
            if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('### Step 2: Select Industry Segment')
    i_cols = st.columns(5)
    inds = {"Fin": "🏦 Financial", "Ret": "🛒 Retail", "Tel": "📡 Telecoms", "Pub": "🏛️ Public", "Min": "⛏️ Mining"}
    for i, (k, v) in enumerate(inds.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"i_{k}"): st.session_state.ind = v; st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# 5. ORCHESTRATION ENGINE
if "ind" in st.session_state:
    frictions = st.text_area("Define Executive Friction Points:", placeholder="e.g. KYC latency leading to client drop-off...")
    
    if st.button("⚡ GENERATE VISION & ROADMAP", type="primary"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            target = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
            model = genai.GenerativeModel(target)
            
            prompt = f"""
            Industry: {st.session_state.ind} | Maturity: {st.session_state.maturity}
            Context: {load_knowledge()}
            Friction: {frictions}
            
            Generate an executive strategy:
            1. [VISION] Bold AI North Star vision statement.
            2. [METRIC] Realistic Before vs After metric (e.g. 5 days to 2 hours).
            3. [MONTH1], [MONTH2], [MONTH3] Detailed bullets for Foundations, Value Drops, and Agentic Scaling.
            """
            
            with st.spinner("Orchestrating Value..."):
                res = model.generate_content(prompt).text
                
                # EXECUTIVE DASHBOARD RENDERING
                vision = res.split("[VISION]")[1].split("[METRIC]")[0].strip()
                metric = res.split("[METRIC]")[1].split("[MONTH1]")[0].strip()
                
                st.markdown(f'<div class="vision-header"><h1>{vision}</h1></div>', unsafe_allow_html=True)
                
                m1, m2, m3 = st.columns(3)
                with m1:
                    st.markdown(f'<div class="exec-card"><h3>🏗️ Month 1</h3><div class="metric-box"><b>Goal:</b> Foundations</div>{res.split("[MONTH1]")[1].split("[MONTH2]")[0]}</div>', unsafe_allow_html=True)
                with m2:
                    st.markdown(f'<div class="exec-card"><h3>🚀 Month 2</h3><div class="metric-box"><b>Goal:</b> Value Drops</div>{res.split("[MONTH2]")[1].split("[MONTH3]")[0]}</div>', unsafe_allow_html=True)
                with m3:
                    st.markdown(f'<div class="exec-card"><h3>🤖 Month 3</h3><div class="metric-box"><b>Goal:</b> Agentic AI</div>{res.split("[MONTH3]")[1]}</div>', unsafe_allow_html=True)
                
                st.success(f"**90-Day Impact Projection:** {metric}")

        except Exception as e:
            st.error(f"Engine Error: {e}")
