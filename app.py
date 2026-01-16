import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# STEP 1: MATURITY
st.markdown('<p class="step-header">Step 1: Diagnose Maturity</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "🔭 EXPLORER", "Scaler": "🚀 SCALER", "Innovator": "🤖 INNOVATOR"}
for i, (k, v) in enumerate(m_opts.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button(v, key=f"m_{k}"): st.session_state.maturity = k; st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

# STEP 2: CONTEXT
if "maturity" in st.session_state:
    st.markdown('<p class="step-header">Step 2: Design Context</p>', unsafe_allow_html=True)
    industry = st.text_input("Industry Segment", placeholder="e.g. Financial Services")
    frictions = st.text_area("Identify the top friction points:", height=150)

    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
        res = run_orchestrator(industry, st.session_state.maturity, frictions)
        st.markdown("---")
        st.markdown('<p class="title-text" style="font-size: 2rem !important;">Acceleration Roadmap</p>', unsafe_allow_html=True)
        st.write(res)
