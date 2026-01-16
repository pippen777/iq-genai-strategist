import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

# Ensure page config is the absolute first line
st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# 01 / MATURITY
st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "EXPLORER", "Scaler": "SCALER", "Innovator": "INNOVATOR"}

for i, (key, label) in enumerate(m_opts.items()):
    with m_cols[i]:
        display_label = f"{label} ✓" if st.session_state.get("maturity") == key else label
        if st.button(display_label, key=f"mat_{key}"):
            st.session_state.maturity = key
            st.rerun()

if "maturity" not in st.session_state:
    st.stop()

# 02 / SELECT INDUSTRY
st.markdown('<p class="step-header">02 / SELECT INDUSTRY</p>', unsafe_allow_html=True)
i_cols = st.columns(5)
i_opts = {"Fin": "FINANCIAL", "Ret": "RETAIL", "Tel": "TELECOMS", "Pub": "PUBLIC", "Min": "MINING"}

for i, (key, label) in enumerate(i_opts.items()):
    with i_cols[i]:
        display_label = f"{label} ✓" if st.session_state.get("ind") == label else label
        if st.button(display_label, key=f"ind_{key}"):
            st.session_state.ind = label
            st.rerun()

if "ind" not in st.session_state:
    st.stop()

# 03 / STRATEGIC CONTEXT
st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
frictions = st.text_area("Identify the top friction points:", height=150, placeholder="Define the business blocker...")

# RESTORED: THE KINETIC GENERATE BUTTON
if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    if not frictions:
        st.warning("Please provide context to ground the GESHIDO strategy.")
    else:
        # THE HIGH-END LOADING SEQUENCE
        progress_bar = st.progress(0)
        status = st.empty()
        
        status.markdown('<p class="label-accent">Synthesizing GESHIDO® Strategy...</p>', unsafe_allow_html=True)
        progress_bar.progress(30)
        
        res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
        
        progress_bar.progress(100)
        status.empty()
        progress_bar.empty()
        
        st.markdown("---")
        # RENDER THE DASHBOARD
        st.markdown(res, unsafe_allow_html=True)
        st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")
