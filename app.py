# ... (Page config and imports)

# 01 / MATURITY
st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
m_opts = {"Explorer": "EXPLORER", "Scaler": "SCALER", "Innovator": "INNOVATOR"}

for i, (key, label) in enumerate(m_opts.items()):
    with m_cols[i]:
        # HIDDEN SELECTION MARKER
        if st.session_state.get("maturity") == key:
            st.markdown('<p class="selection-marker">SELECTED</p>', unsafe_allow_html=True)
        
        if st.button(label, key=f"mat_{key}"):
            st.session_state.maturity = key
            st.rerun()

# 02 / INDUSTRY
if "maturity" in st.session_state:
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

# ... (Step 03 and Orchestration logic remain the same)
