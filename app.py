import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & LUXURY ARCHITECTURE
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_luxury_branding():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background: #020408 !important; 
        background-image: radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.08) 0, transparent 50%), 
                          radial-gradient(at 100% 100%, rgba(142, 45, 226, 0.08) 0, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important; 
    }
    
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 3.2rem !important; font-weight: 800 !important; letter-spacing: -1.5px;
    }

    /* PREMIUM DASHBOARD ELEMENTS */
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); 
        backdrop-filter: blur(15px);
        padding: 45px; border-radius: 2px; border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center; margin: 30px 0;
    }
    
    .phase-card { 
        background: rgba(255, 255, 255, 0.01); 
        padding: 30px; border-top: 2px solid rgba(0, 173, 239, 0.4);
        min-height: 420px; transition: all 0.3s ease;
    }

    .label-accent { 
        color: #00ADEF; text-transform: uppercase; font-size: 0.7rem; 
        font-weight: 700; letter-spacing: 3px; margin-bottom: 10px;
    }

    /* KINETIC BUTTONS: FIXED HOVER & SELECTION */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.03) !important;
        color: rgba(255, 255, 255, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 0px !important; height: 50px !important;
        text-transform: uppercase; letter-spacing: 2px; font-size: 0.75rem !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button:hover {
        color: #ffffff !important;
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.05) !important;
    }

    .selected-glow div.stButton > button {
        background: #ffffff !important; color: #020408 !important;
        border: none !important; font-weight: 700 !important;
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.25) !important;
    }

    .stTextArea textarea { background: rgba(255,255,255,0.02) !important; color: #fff !important; border: 1px solid rgba(255,255,255,0.1) !important; }
    </style>
    """, unsafe_allow_html=True)

apply_luxury_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">STRATEGY VAULT</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Consultant Access Key", type="password")
    if st.button("VERIFY"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

st.markdown('<p class="title-text">ORCHESTRATOR</p>', unsafe_allow_html=True)

# 3. SELECTORS
st.markdown('<br><p class="label-accent">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
for i, (k, v) in enumerate({"Explorer": "Explorer", "Scaler": "Scaler", "Innovator": "Innovator"}.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
        if st.button(v, key=f"mat_{k}"): st.session_state.maturity = k; st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('<br><p class="label-accent">02 / INDUSTRY VERTICAL</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    for i, (k, v) in enumerate({"Fin": "Financial", "Ret": "Retail", "Tel": "Telecoms", "Pub": "Public", "Min": "Mining"}.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"): st.session_state.ind = v; st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# 4. GROUNDED ENGINE (NO HALLUCINATIONS)
if "ind" in st.session_state:
    frictions = st.text_area("EXECUTIVE FRICTION POINTS:", placeholder="e.g. 5-day KYC latency costing 20% lead loss...")
    
    if st.button("ORCHESTRATE ROADMAP", type="primary"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # Auto-discovery fix for 404
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
            
            prompt = f"""
            System: IQ Business Senior Strategist. Methodology: GESHIDO® (Foundations Monthly, Value Weekly). 
            Constraint: Ground all impact projections ONLY in the specific friction provided. Do not invent unrelated data.
            
            Input: {st.session_state.ind} sector, {st.session_state.maturity} maturity. Friction: {frictions}.
            
            Structure:
            [VISION] 1-sentence high-level vision.
            [KPI] The specific 'Before' vs 'After' for the FRICTION provided.
            [M1], [M2], [M3] Phased 12-week roadmap.
            No markdown stars (**).
            """
            
            with st.spinner("SYNTHESIZING..."):
                res = model.generate_content(prompt).text
                
                def extract(text, tag, end_tag=None):
                    start = text.find(tag) + len(tag)
                    end = text.find(end_tag) if end_tag else len(text)
                    return text[start:end].replace("**", "").strip()

                st.markdown(f'<div class="vision-container"><h1 style="font-weight:300; font-size: 2.3rem;">{extract(res, "[VISION]", "[KPI]")}</h1></div>', unsafe_allow_html=True)
                
                st.markdown(f'<div style="text-align:center; margin-bottom:50px;"><p class="label-accent">STRATEGIC IMPACT PROJECTION</p><h2 style="color:#00ADEF; font-size:2.4rem; font-weight:800;">{extract(res, "[KPI]", "[M1]")}</h2></div>', unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 01 / FOUNDATION</p><div style="font-size:0.9rem; line-height:1.6; color:rgba(255,255,255,0.75);">{extract(res, "[M1]", "[M2]")}</div></div>', unsafe_allow_html=True)
                with c2: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 02 / VELOCITY</p><div style="font-size:0.9rem; line-height:1.6; color:rgba(255,255,255,0.75);">{extract(res, "[M2]", "[M3]")}</div></div>', unsafe_allow_html=True)
                with c3: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 03 / AGENTIC</p><div style="font-size:0.9rem; line-height:1.6; color:rgba(255,255,255,0.75);">{extract(res, "[M3]")}</div></div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"ENGINE STATUS: {e}")
