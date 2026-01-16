import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# STEP 1: MATURITY
st.markdown('<p style="color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:2px; font-size:0.8rem;">Step 1: Diagnose Maturity</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "EXPLORER", "Scaler": "SCALER", "Innovator": "INNOVATOR"}

for i, (key, label) in enumerate(m_opts.items()):
    with m_cols[i]:
        # If active, we add a hidden marker character '✓'
        display_label = f"{label} ✓" if st.session_state.get("maturity") == key else label
        if st.button(display_label, key=f"mat_{key}"):
            st.session_state.maturity = key
            st.rerun()

# STEP 2: INDUSTRY
if "maturity" in st.session_state:
    st.markdown('<p style="color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:2px; font-size:0.8rem; margin-top:30px;">Step 2: Industry Segment</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    i_opts = {"Fin": "FINANCIAL", "Ret": "RETAIL", "Tel": "TELECOMS", "Pub": "PUBLIC", "Min": "MINING"}
    
    for i, (key, label) in enumerate(i_opts.items()):
        with i_cols[i]:
            display_label = f"{label} ✓" if st.session_state.get("ind") == label else label
            if st.button(display_label, key=f"ind_{key}"):
                st.session_state.ind = label
                st.rerun()

# STEP 3: CONTEXT
if "ind" in st.session_state:
    st.markdown('<p style="color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:2px; font-size:0.8rem; margin-top:30px;">Step 3: Define Friction</p>', unsafe_allow_html=True)
    frictions = st.text_area("Identify strategic friction points:", height=150)

if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    # Ensure ind and maturity are pulled from session_state
    res = run_orchestrator(
        st.session_state.ind, 
        st.session_state.maturity, 
        frictions
    )
    st.markdown("---")
    st.markdown(f'<p class="title-text" style="font-size: 2rem !important;">Acceleration Roadmap</p>', unsafe_allow_html=True)
    st.write(res)
