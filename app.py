import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# STEP 1: MATURITY DIAGNOSTIC
st.markdown('<p class="step-header">Step 1: Diagnose Maturity</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "🔭 EXPLORER", "Scaler": "🚀 SCALER", "Innovator": "🤖 INNOVATOR"}
for i, (k, v) in enumerate(m_opts.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button(v, key=f"m_{k}"): 
            st.session_state.maturity = k
            st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

# STEP 2: INDUSTRY SEGMENT BUTTONS
if "maturity" in st.session_state:
    st.markdown('<p class="step-header">Step 2: Select Industry Segment</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    i_opts = {
        "Fin": "🏦 FINANCIAL", 
        "Ret": "🛒 RETAIL", 
        "Tel": "📡 TELECOMS", 
        "Pub": "🏛️ PUBLIC", 
        "Min": "⛏️ MINING"
    }
    for i, (k, v) in enumerate(i_opts.items()):
        with i_cols[i]:
            # This wrapper applies the 'Selected' Neon Glow from your styles.py
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"): 
                st.session_state.ind = v
                st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

# STEP 3: STRATEGIC CONTEXT & GENERATION
if "ind" in st.session_state:
    st.markdown('<p class="step-header">Step 3: Define Friction</p>', unsafe_allow_html=True)
    frictions = st.text_area("Identify the top friction points or value pools:", height=150, placeholder="e.g., 5-day KYC latency costing 20% lead loss...")

    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
        if not frictions:
            st.warning("Please provide strategic friction context.")
        else:
            # Passes industry and maturity to the grounded brain.py
            res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
            st.markdown("---")
            st.markdown('<p class="title-text" style="font-size: 2rem !important;">Acceleration Roadmap</p>', unsafe_allow_html=True)
            st.write(res)
            st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")
