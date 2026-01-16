import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

# ... (Keep your Maturity and Industry button logic here) ...

# 03 / STRATEGIC CONTEXT
st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
frictions = st.text_area("Identify strategic friction points:", height=150)

if "orchestration_result" not in st.session_state:
    st.session_state.orchestration_result = None

if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    with st.spinner("Synthesizing Intelligence..."):
        st.session_state.orchestration_result = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)

if st.session_state.orchestration_result:
    st.markdown("---")
    st.markdown(st.session_state.orchestration_result, unsafe_allow_html=True)
    
    # THE "MAGIC" PIVOT BOX
    st.markdown('<p class="step-header">STRATEGY PIVOT: CHALLENGE THE ENGINE</p>', unsafe_allow_html=True)
    pivot_input = st.text_input("What if the budget is cut? What if compliance says no?", key="pivot")
    
    if st.button("RE-ORCHESTRATE"):
        with st.spinner("Adapting Strategy..."):
            st.session_state.orchestration_result = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions, pivot_input)
            st.rerun()
