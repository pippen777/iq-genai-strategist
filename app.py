import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & HIGH-END BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');
    
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { 
        background-color: #05070a !important; 
        background-image: radial-gradient(circle at 80% 20%, rgba(142, 45, 226, 0.15), transparent), 
                          radial-gradient(circle at 20% 80%, rgba(0, 173, 239, 0.15), transparent) !important;
        color: #ffffff !important; 
        font-family: 'Inter', sans-serif !important; 
    }
    
    .title-text { 
        background: linear-gradient(90deg, #00ADEF, #8E2DE2, #F02FC2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-size: 3.5rem !important; 
        font-weight: 800 !important; 
        letter-spacing: -2px;
        margin-bottom: 0px;
    }

    /* GLASSMORPHISM CARDS */
    .vision-header { 
        background: rgba(255, 255, 255, 0.03); 
        backdrop-filter: blur(10px);
        padding: 50px; 
        border-radius: 1px; 
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center; 
        margin: 40px 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .exec-card { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 30px; 
        border-radius: 1px; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        min-height: 450px;
        transition: transform 0.3s ease;
    }
    .exec-card:hover { border: 1px solid rgba(0, 173, 239, 0.4); }

    .card-label { 
        color: #00ADEF; 
        text-transform: uppercase; 
        font-size: 0.7rem; 
        font-weight: 700; 
        letter-spacing: 3px; 
        margin-bottom: 20px; 
    }

    /* MODERN SELECTOR BUTTONS */
    div.stButton > button {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 0px !important;
        height: 50px !important;
        width: 100% !important;
        font-weight: 400 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.75rem !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    }
    
    div.stButton > button:hover {
        color: white !important;
        border-color: white !important;
        background: rgba(255, 255, 255, 0.05) !important;
    }

    /* THE SELECTED STATE GLOW */
    .selected-glow div.stButton > button {
        background: white !important;
        color: black !important;
        border: none !important;
        font-weight: 700 !important;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.4) !important;
    }

    .stTextArea textarea { 
        background: rgba(255,255,255,0.02) !important; 
        color: white !important; 
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
if "password_correct" not in st.session_state:
    st.markdown('<h1 class="title-text">STRATEGY VAULT</h1>', unsafe_allow_html=True)
    pwd = st.text_input("Enter Access Key", type="password")
    if st.button("AUTHENTICATE"):
        if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
            st.session_state["password_correct"] = True
            st.rerun()
    st.stop()

st.markdown('<p class="title-text">ORCHESTRATOR</p>', unsafe_allow_html=True)

# 3. INPUT SECTIONS
st.markdown('<br><p class="card-label">01 / AI MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
opts = {"Explorer": "Explorer", "Scaler": "Scaler", "Innovator": "Innovator"}
for i, (k, v) in enumerate(opts.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
        if st.button(v, key=f"mat_{k}"):
            st.session_state.maturity = k
            st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('<br><p class="card-label">02 / INDUSTRY SEGMENT</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    inds = {"Fin": "Financial", "Ret": "Retail", "Tel": "Telecoms", "Pub": "Public", "Min": "Mining"}
    for i, (k, v) in enumerate(inds.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-glow">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"):
                st.session_state.ind = v
                st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# 4. FAIL-SAFE ENGINE
if "ind" in st.session_state:
    frictions = st.text_area("STRATEGIC FRICTION POINTS:", placeholder="Define the business blocker...")
    
    if st.button("ORCHESTRATE STRATEGY", type="primary"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            
            # Dynamic Model Discovery to avoid 404
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
            
            model = genai.GenerativeModel(target_model)
            
            prompt = f"""
            System: IQ Business Senior Partner.
            Context: Industry {st.session_state.ind}, Maturity {st.session_state.maturity}.
            Problem: {frictions}
            
            Task: Provide a 90-day strategy.
            Format:
            [VISION] One sentence bold vision.
            [METRIC] Before vs After impact.
            [MONTH1], [MONTH2], [MONTH3] 4 bullets each.
            No markdown stars (**). Use <b> tags for emphasis.
            """
            
            with st.spinner("SYNTHESIZING..."):
                res = model.generate_content(prompt).text
                
                def extract(text, tag, end_tag=None):
                    start = text.find(tag) + len(tag)
                    end = text.find(end_tag) if end_tag else len(text)
                    return text[start:end].replace("**", "").strip()

                st.markdown(f'<div class="vision-header"><h1 style="font-weight:300; font-size: 2.2rem; line-height:1.2;">{extract(res, "[VISION]", "[METRIC]")}</h1></div>', unsafe_allow_html=True)
                
                st.markdown(f'<div style="text-align:center; margin-bottom:60px;"><p class="card-label">PROJECTED IMPACT</p><h2 style="color:#F02FC2; font-size:2.5rem; font-weight:800;">{extract(res, "[METRIC]", "[MONTH1]")}</h2></div>', unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f'<div class="exec-card"><p class="card-label">PHASE 01 / FOUNDATION</p><div style="font-size:0.95rem; line-height:1.6; color:rgba(255,255,255,0.8);">{extract(res, "[MONTH1]", "[MONTH2]")}</div></div>', unsafe_allow_html=True)
                with c2: st.markdown(f'<div class="exec-card"><p class="card-label">PHASE 02 / VELOCITY</p><div style="font-size:0.95rem; line-height:1.6; color:rgba(255,255,255,0.8);">{extract(res, "[MONTH2]", "[MONTH3]")}</div></div>', unsafe_allow_html=True)
                with c3: st.markdown(f'<div class="exec-card"><p class="card-label">PHASE 03 / AGENTIC</p><div style="font-size:0.95rem; line-height:1.6; color:rgba(255,255,255,0.8);">{extract(res, "[MONTH3]")}</div></div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"ENGINE STATUS: {e}")
