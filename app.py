import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & HIGH-END ARCHITECTURE
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background: #020408 !important; 
        background-image: radial-gradient(at 0% 0%, rgba(0, 173, 239, 0.1) 0, transparent 50%), 
                          radial-gradient(at 100% 100%, rgba(240, 47, 194, 0.1) 0, transparent 50%) !important;
        font-family: 'Outfit', sans-serif !important; 
    }
    
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 3.5rem !important; 
        font-weight: 900 !important; 
        letter-spacing: -2px;
        margin-bottom: 0px;
    }

    /* PREMIUM GLASS DASHBOARD */
    .vision-container { 
        background: rgba(255, 255, 255, 0.02); 
        backdrop-filter: blur(20px);
        padding: 60px; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center; 
        margin: 40px 0;
    }
    
    .phase-card { 
        background: rgba(255, 255, 255, 0.01); 
        padding: 40px; 
        border-left: 1px solid rgba(0, 173, 239, 0.3);
        min-height: 480px;
        transition: all 0.4s ease;
    }
    .phase-card:hover { background: rgba(255, 255, 255, 0.03); border-left: 1px solid #F02FC2; }

    .label-accent { 
        color: #00ADEF; 
        text-transform: uppercase; 
        font-size: 0.7rem; 
        font-weight: 700; 
        letter-spacing: 4px; 
    }

    /* KINETIC BUTTONS: Fixes the hover & selection logic */
    div.stButton > button {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 0px !important;
        height: 55px !important;
        font-weight: 400 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div.stButton > button:hover {
        color: #ffffff !important;
        border-color: #00ADEF !important;
        box-shadow: inset 0 0 10px rgba(0, 173, 239, 0.2) !important;
    }

    .selected-glow div.stButton > button {
        background: #ffffff !important;
        color: #020408 !important;
        border: none !important;
        font-weight: 700 !important;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.2) !important;
    }

    .stTextArea textarea { 
        background: transparent !important; 
        color: #ffffff !important; 
        border: 1px solid rgba(255,255,255,0.1) !important;
        font-size: 1.1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">STRATEGY VAULT</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Consultant Access Key", type="password")
    if st.button("VERIFY IDENTITY"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

st.markdown('<p class="title-text">ORCHESTRATOR</p>', unsafe_allow_html=True)

# 3. STRATEGIC INPUTS
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

# 4. GROUNDED ORCHESTRATION ENGINE
if "ind" in st.session_state:
    frictions = st.text_area("EXECUTIVE FRICTION POINTS:", placeholder="Define the business blocker...")
    
    if st.button("ORCHESTRATE ROADMAP", type="primary"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # Auto-discovery to prevent 404
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
            
            # STRICT GROUNDING PROMPT
            prompt = f"""
            Role: IQ Business Lead Strategist. 
            Methodology: GESHIDO® (Foundations Monthly, Value Weekly).
            Constraint: Ground all tasks in South African compliance (POPIA).
            
            Inputs: Industry {st.session_state.ind}, Maturity {st.session_state.maturity}, Friction {frictions}.
            
            Output Structure (Strictly No Markdown Stars):
            [VISION] 1-sentence high-impact vision.
            [IMPACT] Realistic Before vs After metrics.
            [M1], [M2], [M3] 4 bullets each. Month 1 MUST focus on Foundation. Month 3 MUST focus on Agentic Scaling.
            """
            
            with st.spinner("SYNTHESIZING STRATEGY..."):
                res = model.generate_content(prompt).text
                
                def extract(text, tag, end_tag=None):
                    start = text.find(tag) + len(tag)
                    end = text.find(end_tag) if end_tag else len(text)
                    return text[start:end].replace("**", "").strip()

                st.markdown(f'<div class="vision-container"><h1 style="font-weight:300; font-size: 2.5rem;">{extract(res, "[VISION]", "[IMPACT]")}</h1></div>', unsafe_allow_html=True)
                
                st.markdown(f'<div style="text-align:center; margin-bottom:60px;"><p class="label-accent">90-DAY PROJECTED IMPACT</p><h2 style="color:#F02FC2; font-size:2.8rem; font-weight:900; letter-spacing:-1px;">{extract(res, "[IMPACT]", "[M1]")}</h2></div>', unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 01 / FOUNDATION</p><div style="color:rgba(255,255,255,0.7);">{extract(res, "[M1]", "[M2]")}</div></div>', unsafe_allow_html=True)
                with c2: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 02 / VELOCITY</p><div style="color:rgba(255,255,255,0.7);">{extract(res, "[M2]", "[M3]")}</div></div>', unsafe_allow_html=True)
                with c3: st.markdown(f'<div class="phase-card"><p class="label-accent">MONTH 03 / AGENTIC</p><div style="color:rgba(255,255,255,0.7);">{extract(res, "[M3]")}</div></div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"ENGINE STATUS: {e}")
