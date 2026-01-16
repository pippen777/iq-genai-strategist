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
# ... (Maturity and Industry button loops remain the same)

# ONLY show Step 3 if both previous selections are made
if "maturity" in st.session_state and "ind" in st.session_state:
    st.markdown('<p class="step-header">Step 3: Define Strategic Friction</p>', unsafe_allow_html=True)
    
    # Use a unique key for the text area to prevent ghost rendering
    frictions = st.text_area(
        "Identify the top friction points or value pools:", 
        height=150, 
        placeholder="e.g. Manual claims processing is causing a 14-day delay...",
        key="friction_input"
    )

    # The Roadmap button now only appears when we have data
    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary", key="final_orchestrate"):
        if not frictions:
            st.warning("Please provide context to ground the GESHIDO strategy.")
        else:
            with st.spinner("Synthesizing IQ Strategy..."):
                res = run_orchestrator(
                    st.session_state.ind, 
                    st.session_state.maturity, 
                    frictions
                )
                st.markdown("---")
                # Restore the high-end title for the output
                st.markdown('<p class="title-text" style="font-size: 2.2rem !important;">Acceleration Roadmap</p>', unsafe_allow_html=True)
                st.write(res)
                st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")

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
