import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# 01 / MATURITY
st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "EXPLORER", "Scaler": "SCALER", "Innovator": "INNOVATOR"}

for i, (key, label) in enumerate(m_opts.items()):
    with m_cols[i]:
        is_selected = st.session_state.get("maturity") == key
        if st.button(f"{label} ✓" if is_selected else label, key=f"mat_{key}"):
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
        is_selected = st.session_state.get("ind") == label
        if st.button(f"{label} ✓" if is_selected else label, key=f"ind_{key}"):
            st.session_state.ind = label
            st.rerun()

if "ind" not in st.session_state:
    st.stop()

# 03 / STRATEGIC CONTEXT
st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
frictions = st.text_area("Identify strategic friction points:", height=150, placeholder="Define the business blocker...")

# Replace your button logic in app.py with this:
if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    if not frictions:
        st.warning("Provide context for the GESHIDO® engine.")
    else:
        # PULSE LOADING
        with st.spinner("Synthesizing Value Streams & Mining GESHIDO® Insights..."):
            res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
        
        st.markdown("---")
        st.markdown(res, unsafe_allow_html=True)
        # Add the closing workshop CTA we built
        st.markdown("<div class='aha-box'><p style='font-size:1.2rem;'>Ready to recapture this value?</p></div>", unsafe_allow_html=True)
