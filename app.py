import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

# 1. SETUP
st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

# 2. STEP 01: MATURITY SELECTOR
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

# 3. STEP 02: INDUSTRY SELECTOR
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

# 4. STEP 03: STRATEGIC CONTEXT
st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
frictions = st.text_area("Identify strategic friction points:", height=150, placeholder="Describe the business blocker...")

# 5. ORCHESTRATION LOGIC
if "orchestration_result" not in st.session_state:
    st.session_state.orchestration_result = None

if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    if not frictions:
        st.warning("Please provide context to ground the strategy.")
    else:
        with st.spinner("Synthesizing Intelligence & GESHIDO® Logic..."):
            st.session_state.orchestration_result = run_orchestrator(
                st.session_state.ind, 
                st.session_state.maturity, 
                frictions
            )

# 6. DISPLAY RESULTS & PIVOT
if st.session_state.orchestration_result:
    st.markdown("---")
    st.markdown(st.session_state.orchestration_result, unsafe_allow_html=True)
    
    # THE "INTELLIGENCE LAB" PIVOT
    st.markdown('<p class="step-header">STRATEGY PIVOT: CHALLENGE THE ENGINE</p>', unsafe_allow_html=True)
    st.info("The AI Strategy Partner is ready to refine the plan. Ask about budget cuts, compliance risks, or alternative approaches.")
    
    pivot_input = st.text_input("Example: 'What if compliance bans SMS?' or 'Reduce budget by 50%'", key="pivot_box")
    
    if st.button("RE-ORCHESTRATE STRATEGY"):
        with st.spinner("Adapting Intelligence..."):
            st.session_state.orchestration_result = run_orchestrator(
                st.session_state.ind, 
                st.session_state.maturity, 
                frictions, 
                pivot_input
            )
            st.rerun()

    st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")
