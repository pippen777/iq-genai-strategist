import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

# 1. CRITICAL: Page config must be first
st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# 01 / MATURITY
st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "EXPLORER", "Scaler": "SCALER", "Innovator": "INNOVATOR"}

for i, (key, label) in enumerate(m_opts.items()):
    with m_cols[i]:
        # Stable CSS hook instead of checkmark character
        if st.session_state.get("maturity") == key:
            st.markdown('<p class="selection-marker">SELECTED</p>', unsafe_allow_html=True)
        
        if st.button(label, key=f"mat_{key}"):
            st.session_state.maturity = key
            st.rerun()

if "maturity" not in st.session_state:
    st.stop()

# 02 / INDUSTRY
st.markdown('<p class="step-header">02 / SELECT INDUSTRY</p>', unsafe_allow_html=True)
i_cols = st.columns(5)
i_opts = {"Fin": "FINANCIAL", "Ret": "RETAIL", "Tel": "TELECOMS", "Pub": "PUBLIC", "Min": "MINING"}

for i, (key, label) in enumerate(i_opts.items()):
    with i_cols[i]:
        if st.session_state.get("ind") == label:
            st.markdown('<p class="selection-marker">SELECTED</p>', unsafe_allow_html=True)
        
        if st.button(label, key=f"ind_{key}"):
            st.session_state.ind = label
            st.rerun()

if "ind" not in st.session_state:
    st.stop()

# 03 / STRATEGIC CONTEXT
st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
frictions = st.text_area("Identify strategic friction points:", height=150, placeholder="Define the business blocker...")

if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    if not frictions:
        st.warning("Please provide context to ground the GESHIDO strategy.")
    else:
        progress_bar = st.progress(0)
        status = st.empty()
        status.markdown('<p class="label-accent">Synthesizing IQ Strategy...</p>', unsafe_allow_html=True)
        progress_bar.progress(30)
        
        res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
        
        progress_bar.progress(100)
        status.empty()
        progress_bar.empty()
        
        st.markdown("---")
        st.markdown(res, unsafe_allow_html=True)
        st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")
