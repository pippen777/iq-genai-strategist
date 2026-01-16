import streamlit as st
from styles import apply_iq_styles
from brain import run_orchestrator

# 1. SETUP & THEME
st.set_page_config(page_title="IQ Orchestrator", layout="wide")
apply_iq_styles()

# 2. PASSWORD PROTECTION
def check_password():
    """Returns True if the user had the correct password."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)
        st.markdown('<p class="step-header">Secure Access Required</p>', unsafe_allow_html=True)
        
        # Centered login box using a column trick
        _, col, _ = st.columns([1, 1, 1])
        with col:
            pwd = st.text_input("Enter Passcode:", type="password")
            if st.button("AUTHENTICATE"):
                if pwd == st.secrets["APP_PASSWORD"]: # Set this in your Streamlit Secrets
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid Credentials")
        return False
    return True

if check_password():
    # --- EVERYTHING BELOW IS YOUR EXISTING APP CODE ---
    st.markdown('<h1 class="title-text">Orchestrator</h1>', unsafe_allow_html=True)

    # 3. STEP 01: MATURITY
    st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
    # ... (rest of your app.py code)
