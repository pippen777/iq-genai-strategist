# --- app.py ---
import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)
        _, col, _ = st.columns([1, 1, 1])
        with col:
            pwd = st.text_input("Enter Passcode:", type="password")
            if st.button("AUTHENTICATE"):
                # Make sure "APP_PASSWORD" is set in your Streamlit Secrets!
                if pwd == st.secrets["APP_PASSWORD"]:
                    st.session_state.authenticated = True
                    st.rerun() # Forces the app to refresh and show the buttons
                else:
                    st.error("Invalid Credentials")
        return False
    return True

if check_password():
    # RESTORE THE COOLER TITLE
    st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

    # STEP 01: MATURITY (Now explicitly rendered after login)
    st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
    m_cols = st.columns(3)
    m_opts = ["Explorer", "Scaler", "Innovator"]
    
    for i, opt in enumerate(m_opts):
        # Highlighting the selected button
        label = f"{opt} ✓" if st.session_state.get("mat") == opt else opt
        if m_cols[i].button(label, key=f"btn_m_{opt}"):
            st.session_state.mat = opt
            st.rerun()

    # STEP 02: INDUSTRY
    if "mat" in st.session_state:
        st.markdown('<p class="step-header">02 / SELECT INDUSTRY</p>', unsafe_allow_html=True)
        i_cols = st.columns(5)
        i_opts = ["Financial", "Retail", "Telecoms", "Public", "Mining"]
        for i, opt in enumerate(i_opts):
            label = f"{opt} ✓" if st.session_state.get("ind") == opt else opt
            if i_cols[i].button(label, key=f"btn_i_{opt}"):
                st.session_state.ind = opt
                st.rerun()

    # STEP 03: FRICTION (Only shows once Industry is selected)
    if "ind" in st.session_state:
        st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
        frictions = st.text_area("Identify strategic friction points:", height=150)
        
        if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
            with st.spinner("Analyzing tensions and modeling ROI..."):
                st.session_state.res = run_orchestrator(st.session_state.ind, st.session_state.mat, frictions)
                st.rerun()
   
# --- Bottom of app.py ---

if st.session_state.get("res"):
    st.markdown("---")
    # This renders the Roadmap, Executive Brief, and Reasoning Engine
    st.markdown(st.session_state.res, unsafe_allow_html=True)
    
    st.markdown('<p class="step-header">STRATEGY PIVOT: CHALLENGE THE ENGINE</p>', unsafe_allow_html=True)
    
    # We use a container to ensure the pivot elements stay together
    with st.container():
        pivot_input = st.text_input("What if the CRO cuts the data pool? What if compliance says no?", key="strategy_pivot_input")
        
        if st.button("RE-ORCHESTRATE STRATEGY"):
            if pivot_input:
                with st.spinner("Adapting Logic and Recalculating ROI..."):
                    # We pass the original frictions + the new pivot feedback
                    new_res = run_orchestrator(
                        st.session_state.ind, 
                        st.session_state.mat, 
                        frictions, 
                        user_feedback=pivot_input
                    )
                    st.session_state.res = new_res
                    st.rerun() # Force refresh to show the adapted strategy
