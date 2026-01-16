import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & LUXURY BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background: #05070a !important; 
        background-image: radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.1) 0, transparent 50%), 
                          radial-gradient(at 100% 100%, rgba(142, 45, 226, 0.1) 0, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important; 
    }
    
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 3.5rem !important; font-weight: 900 !important; letter-spacing: -2px;
    }

    /* THE BUTTON REVOLUTION */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 4px !important;
        height: 60px !important;
        width: 100% !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem !important;
    }
    
    /* HOVER STATE: Beautiful IQ Blue Glow */
    div.stButton > button:hover {
        background: rgba(0, 173, 239, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid #00ADEF !important;
        box-shadow: 0 0 20px rgba(0, 173, 239, 0.4) !important;
        transform: translateY(-2px);
    }

    /* SELECTED STATE: Persistent Gradient */
    .selected-btn div.stButton > button {
        background: linear-gradient(90deg, #00ADEF, #8E2DE2) !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 700 !important;
        box-shadow: 0 0 30px rgba(142, 45, 226, 0.5) !important;
    }

    /* DASHBOARD ELEMENTS */
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); 
        backdrop-filter: blur(20px);
        padding: 50px; border-radius: 4px; border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center; margin: 30px 0;
    }
    .phase-card { 
        background: rgba(255, 255, 255, 0.01); 
        padding: 30px; border-radius: 4px; border-left: 3px solid #00ADEF;
        min-height: 400px;
    }
    .label-accent { color: #00ADEF; text-transform: uppercase; font-size: 0.7rem; font-weight: 700; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">STRATEGY VAULT</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Access Key", type="password")
    if st.button("AUTHENTICATE"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)

# 3. SELECTORS WITH PERSISTENT COLOR
st.markdown('<br><p class="label-accent">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
for i, (k, v) in enumerate({"Explorer": "Explorer", "Scaler": "Scaler", "Innovator": "Innovator"}.items()):
    with m_cols[i]:
        # WRAPPER FOR PERSISTENCE
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button(v, key=f"mat_{k}"):
            st.session_state.maturity = k
            st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('<br><p class="label-accent">02 / SELECT INDUSTRY</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    for i, (k, v) in enumerate({"Fin": "Financial", "Ret": "Retail", "Tel": "Telecoms", "Pub": "Public", "Min": "Mining"}.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"):
                st.session_state.ind = v
                st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# 4. STABLE ENGINE
if "ind" in st.session_state:
    frictions = st.text_area("EXECUTIVE FRICTION:", placeholder="e.g. 5-day KYC latency...")
    
    if st.button("ORCHESTRATE STRATEGY", type="primary"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # Discovery logic to prevent 404
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
            model = genai.GenerativeModel(target_model)
            
            prompt = f"""
            System: IQ Business Senior Strategist. Methodology: GESHIDO® (Foundations Monthly, Value Weekly). 
            Input: {st.session_state.ind} sector, {st.session_state.maturity} maturity. Friction: {frictions}.
            Required Format (No stars **):
            [VISION] 1-sentence bold vision.
            [KPI] BEFORE vs AFTER metrics for the specific friction.
            [M1], [M2], [M3] 4 bullets each.
            """
            
            with st.spinner("SYNTHESIZING..."):
                res = model.generate_content(prompt).text
                
                def extract(text, tag, end_tag=None):
                    start = text.find(tag) + len(tag)
                    end = text.find(end_tag) if end_tag else len(text)
                    return text[start:end].replace("**", "").strip()

                st.markdown(f'<div class="vision-container"><h1 style="font-weight:300; font-size: 2.3rem;">{extract(res, "[VISION]", "[KPI]")}</h1></div>', unsafe_allow_html=True)
                
                st.markdown(f'<div style="text-align:center; margin-bottom:50px;"><p class="label-accent">90-DAY IMPACT</p><h2 style="color:#00ADEF; font-size:2.8rem; font-weight:800;">{extract(res, "[KPI]", "[M1]")}</h2></div>', unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 01 / FOUNDATION</p>{extract(res, "[M1]", "[M2]")}</div>', unsafe_allow_html=True)
                with c2: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 02 / VELOCITY</p>{extract(res, "[M2]", "[M3]")}</div>', unsafe_allow_html=True)
                with c3: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 03 / AGENTIC</p>{extract(res, "[M3]")}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"ENGINE STATUS: {e}")
