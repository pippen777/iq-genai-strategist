import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & HIGH-OCTANE BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_visionary_branding():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;800;900&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background: radial-gradient(circle at top right, #1a1b3a, #05070a) !important; 
        color: #ffffff !important; 
        font-family: 'Outfit', sans-serif !important; 
    }
    
    /* THE GLOW TITLE */
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 4rem !important; font-weight: 900 !important; letter-spacing: -3px;
        filter: drop-shadow(0 0 10px rgba(142, 45, 226, 0.3));
    }

    /* KINETIC BUTTONS: THE "COOL" SELECTION */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important; height: 65px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        font-weight: 600 !important; text-transform: uppercase; letter-spacing: 1px;
    }
    
    div.stButton > button:hover {
        border-color: #00ADEF !important;
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(0, 173, 239, 0.2) !important;
    }

    /* SELECTED STATE: VIBRANT PULSE */
    .selected-glow div.stButton > button {
        background: linear-gradient(45deg, #00ADEF, #8E2DE2) !important;
        border: none !important;
        box-shadow: 0 0 30px rgba(142, 45, 226, 0.6) !important;
        transform: scale(1.05) !important;
    }

    /* DASHBOARD CARDS */
    .vision-box { 
        background: rgba(255, 255, 255, 0.03); 
        padding: 50px; border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center; margin: 40px 0;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .phase-card { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.05);
        min-height: 400px; transition: border 0.3s ease;
    }
    .phase-card:hover { border: 1px solid #F02FC2; }

    .tag { color: #00ADEF; font-size: 0.75rem; font-weight: 800; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

apply_visionary_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">STRATEGY VAULT</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Consultant Key", type="password")
    if st.button("ORCHESTRATE"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)

# 3. SELECTORS
st.markdown('<br><p class="tag">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
for i, (k, v) in enumerate({"Explorer": "🔭 Explorer", "Scaler": "🚀 Scaler", "Innovator": "🤖 Innovator"}.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
        if st.button(v, key=f"mat_{k}"): st.session_state.maturity = k; st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('<br><p class="tag">02 / SELECT INDUSTRY</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    for i, (k, v) in enumerate({"Fin": "🏦 Financial", "Ret": "🛒 Retail", "Tel": "📡 Telecoms", "Pub": "🏛️ Public", "Min": "⛏️ Mining"}.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"): st.session_state.ind = v; st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# 4. ENGINE
if "ind" in st.session_state:
    frictions = st.text_area("EXECUTIVE FRICTION:", placeholder="e.g. 5-day KYC latency costing 20% conversion...")
    
    if st.button("⚡ GENERATE VISION", type="primary"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # Auto-discovery fix for 404
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
            
            # THE GROUNDED AHA PROMPT
            prompt = f"""
            Role: IQ Business Senior Strategist. Methodology: GESHIDO® (Foundations Monthly, Value Weekly). 
            Input: {st.session_state.ind} sector, {st.session_state.maturity} maturity. Friction: {frictions}.
            
            Required Format:
            [VISION] One sentence of visionary future state.
            [KPI] BEFORE vs AFTER metrics for the specific friction.
            [M1], [M2], [M3] 4 bullets for each phase. 
            No markdown stars (**).
            """
            
            with st.spinner("SYNTHESIZING..."):
                res = model.generate_content(prompt).text
                
                def extract(text, tag, end_tag=None):
                    start = text.find(tag) + len(tag)
                    end = text.find(end_tag) if end_tag else len(text)
                    return text[start:end].replace("**", "").strip()

                st.markdown(f'<div class="vision-box"><h1 style="font-weight:400; font-size: 2.5rem; letter-spacing: -1px;">{extract(res, "[VISION]", "[KPI]")}</h1></div>', unsafe_allow_html=True)
                
                st.markdown(f'<div style="text-align:center; margin-bottom:50px;"><p class="tag">STRATEGIC IMPACT PROJECTION</p><h2 style="color:#00ADEF; font-size:2.8rem; font-weight:800;">{extract(res, "[KPI]", "[M1]")}</h2></div>', unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f'<div class="phase-card"><p class="tag">PHASE 01</p><h3>Foundation</h3>{extract(res, "[M1]", "[M2]")}</div>', unsafe_allow_html=True)
                with c2: st.markdown(f'<div class="phase-card"><p class="tag">PHASE 02</p><h3>Velocity</h3>{extract(res, "[M2]", "[M3]")}</div>', unsafe_allow_html=True)
                with c3: st.markdown(f'<div class="phase-card"><p class="tag">PHASE 03</p><h3>Agentic</h3>{extract(res, "[M3]")}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"ENGINE STATUS: {e}")
