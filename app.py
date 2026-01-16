import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator, clean_extract

st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")
apply_iq_styles()

# SELECTION LOGIC WITH NEON WRAPPER
st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)

st.markdown('<p class="label-accent">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
for i, (k, v) in enumerate({"Explorer": "🔭 Explorer", "Scaler": "🚀 Scaler", "Innovator": "🤖 Innovator"}.items()):
    with m_cols[i]:
        if st.session_state.get("maturity") == k: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button(v, key=f"mat_{k}"): st.session_state.maturity = k; st.rerun()
        if st.session_state.get("maturity") == k: st.markdown('</div>', unsafe_allow_html=True)

if "maturity" in st.session_state:
    st.markdown('<br><p class="label-accent">02 / SELECT INDUSTRY</p>', unsafe_allow_html=True)
    i_cols = st.columns(5)
    for i, (k, v) in enumerate({"Fin": "🏦 Financial", "Ret": "🛒 Retail", "Tel": "📡 Telecoms", "Pub": "🏛️ Public", "Min": "⛏️ Mining"}.items()):
        with i_cols[i]:
            if st.session_state.get("ind") == v: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
            if st.button(v, key=f"ind_{k}"): st.session_state.ind = v; st.rerun()
            if st.session_state.get("ind") == v: st.markdown('</div>', unsafe_allow_html=True)

if "ind" in st.session_state:
    frictions = st.text_area("EXECUTIVE FRICTION POINTS:", placeholder="Define the business blocker...")
    if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
        res = run_orchestrator(st.session_state.ind, st.session_state.maturity, frictions)
        if "ERROR" in res: st.error(res)
        else:
            # DASHBOARD RENDERING
            st.markdown(f'<div class="vision-container"><h1>{clean_extract(res, "[VISION]", "[KPI]")}</h1></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align:center; margin-bottom:50px;"><p class="label-accent">90-DAY IMPACT</p><h2 style="color:#00ADEF; font-size:3rem; font-weight:800;">{clean_extract(res, "[KPI]", "[M1]")}</h2></div>', unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f'<div class="phase-card"><p class="label-accent">PHASE 01 / FOUNDATION</p>{clean_extract(res, "[M1]", "[M2]")}</div>', unsafe_allow_html=True)
            with c2: st.markdown(f'<div class="phase-card"><p class="label-accent">PHASE 02 / VELOCITY</p>{clean_extract(res, "[M2]", "[M3]")}</div>', unsafe_allow_html=True)
            with c3: st.markdown(f'<div class="phase-card"><p class="label-accent">PHASE 03 / AGENTIC</p>{clean_extract(res, "[M3]")}</div>', unsafe_allow_html=True)
