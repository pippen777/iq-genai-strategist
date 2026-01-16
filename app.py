import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Strategy Orchestrator", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# STEP 1: MATURITY (Icons Removed)
st.markdown('<p class="step-header">Step 1: Diagnose Maturity</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "EXPLORER", "Scaler": "SCALER", "Innovator": "INNOVATOR"}

for i, (key, label) in enumerate(m_opts.items()):
    with m_cols[i]:
        # If selected, we drop a hidden text marker that triggers the CSS above
        if st.session_state.get("maturity") == key:
            st.markdown('<p class="selection-marker">ACTIVE_SELECTION</p>', unsafe_allow_html=True)
        
        if st.button(label, key=f"btn_{key}"):
            st.session_state.maturity = key
            st.rerun()

# STEP 2: INDUSTRY (Icons Removed)
if "maturity" in st.session_state:
    st.markdown('<p style="color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:2px; font-size:0.8rem; margin-top:30px;">Step 2: Industry Segment</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    i_opts = {"Fin": "FINANCIAL", "Ret": "RETAIL", "Tel": "TELECOMS", "Pub": "PUBLIC", "Min": "MINING"}
    
    for i, (key, label) in enumerate(i_opts.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == label:
                st.markdown('<div class="locked-selection">', unsafe_allow_html=True)
            
            if st.button(label, key=f"ind_{key}"):
                st.session_state.ind = label
                st.rerun()
                
            if st.session_state.get("ind") == label:
                st.markdown('</div>', unsafe_allow_html=True)

# STEP 3: FRICTION & GENERATION
if "ind" in st.session_state:
    st.markdown('<p style="color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:2px; font-size:0.8rem; margin-top:30px;">Step 3: Define Friction</p>', unsafe_allow_html=True)
    frictions = st.text_area("Identify strategic friction points:", height=150)

    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
        res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
        st.markdown("---")
        st.markdown(res)
