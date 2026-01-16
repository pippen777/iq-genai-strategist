# STEP 3: CONTEXT & GENERATION
st.markdown('<p class="step-header">03 / DEFINE STRATEGIC FRICTION</p>', unsafe_allow_html=True)
frictions = st.text_area("Identify the top friction points or value pools:", height=150, placeholder="Define the business blocker...")

if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
    if not frictions:
        st.warning("Please provide context to ground the GESHIDO strategy.")
    else:
        # THE HIGH-END LOADING SEQUENCE
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Phase 1: Contextualizing
        status_text.markdown('<p class="label-accent">Synthesizing Industry Context...</p>', unsafe_allow_html=True)
        progress_bar.progress(25)
        
        # Phase 2: Grounding (Calls the Brain)
        status_text.markdown('<p class="label-accent">Applying GESHIDO® Framework Grounding...</p>', unsafe_allow_html=True)
        progress_bar.progress(50)
        res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
        
        # Phase 3: Finalizing
        status_text.markdown('<p class="label-accent">Finalizing 12-Week Acceleration Roadmap...</p>', unsafe_allow_html=True)
        progress_bar.progress(90)
        
        # Clear loading elements and show result
        progress_bar.empty()
        status_text.empty()
        
        st.markdown("---")
        st.markdown('<p class="title-text" style="font-size: 2.2rem !important;">Acceleration Roadmap</p>', unsafe_allow_html=True)
        st.write(res)
        st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")
