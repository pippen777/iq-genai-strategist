import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & ENTERPRISE BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { background: #05070a !important; color: #ffffff !important; font-family: 'Inter', sans-serif; }
    .title-text { background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem !important; font-weight: 800 !important; letter-spacing: -1px; }
    
    /* DASHBOARD CARDS */
    .vision-header { background: rgba(255, 255, 255, 0.03); padding: 40px; border-radius: 4px; border: 1px solid rgba(0, 173, 239, 0.3); text-align: center; margin-bottom: 40px; }
    .exec-card { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); padding: 30px; border-radius: 4px; min-height: 400px; }
    .card-label { color: #00ADEF; text-transform: uppercase; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 15px; }
    
    /* BUTTON PERSISTENCE FIX */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 4px !important;
        height: 60px !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        font-size: 0.8rem !important;
    }
    
    /* High-priority CSS to force color on selected state */
    .selected-glow div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 173, 239, 0.4) !important;
    }

    .stTextArea textarea { background: rgba(255,255,255,0.03) !important; color: white !important; border-radius: 4px !important; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">Strategy Vault</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Access Code", type="password")
    if st.button("AUTHENTICATE"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

st.markdown('<p class="title-text">ORCHESTRATOR</p>', unsafe_allow_html=True)

# 3. STEP 1 & 2
st.markdown('<p class="card-label">Step 1: AI Maturity</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
opts = {"Explorer": "Explorer", "Scaler": "Scaler", "Innovator": "Innovator"}
for i, (k, v) in enumerate(opts.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
        if st.button(v, key=f"m_{k}"): st.session_state.maturity = k; st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('<p class="card-label">Step 2: Industry Segment</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    inds = {"Fin": "Financial", "Ret": "Retail", "Tel": "Telecoms", "Pub": "Public", "Min": "Mining"}
    for i, (k, v) in enumerate(inds.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"i_{k}"): st.session_state.ind = v; st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# 4. ENGINE
if "ind" in st.session_state:
    frictions = st.text_area("Define Executive Friction Points:", placeholder="e.g. KYC latency leading to client drop-off...")
    
    if st.button("ORCHESTRATE STRATEGY", type="primary"):
        try:
            # FIX: Forced Stable Initialization
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Role: IQ Business Senior Strategist.
            Industry: {st.session_state.ind} | Maturity: {st.session_state.maturity}
            Friction: {frictions}
            
            Output strictly in this structure (Replace ** with <b> tags):
            [VISION] 1-sentence North Star.
            [METRIC] Before vs After.
            [MONTH1] 4 bullet points.
            [MONTH2] 4 bullet points.
            [MONTH3] 4 bullet points.
            """
            
            with st.spinner("Synthesizing..."):
                res = model.generate_content(prompt).text
                
                # CLEAN EXTRACTION
                def extract(text, tag, end_tag=None):
                    try:
                        start = text.find(tag) + len(tag)
                        end = text.find(end_tag) if end_tag else len(text)
                        clean_text = text[start:end].strip()
                        return clean_text.replace("**", "<b>").replace("</b><b>", "").replace("*", "")
                    except: return "Analysis pending..."

                vision = extract(res, "[VISION]", "[METRIC]")
                metric = extract(res, "[METRIC]", "[MONTH1]")
                m1_val = extract(res, "[MONTH1]", "[MONTH2]")
                m2_val = extract(res, "[MONTH2]", "[MONTH3]")
                m3_val = extract(res, "[MONTH3]")

                # RENDERING DASHBOARD
                st.markdown(f'<div class="vision-header"><h2 style="font-weight:300;">{vision}</h2></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="text-align:center; margin-bottom:40px;"><p class="card-label">90-Day Impact Projection</p><h2 style="color:#00ADEF;">{metric}</h2></div>', unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f'<div class="exec-card"><p class="card-label">Month 1: Foundation</p>{m1_val}</div>', unsafe_allow_html=True)
                with c2: st.markdown(f'<div class="exec-card"><p class="card-label">Month 2: Value Drop</p>{m2_val}</div>', unsafe_allow_html=True)
                with c3: st.markdown(f'<div class="exec-card"><p class="card-label">Month 3: Scaling</p>{m3_val}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"System Error: {e}")
