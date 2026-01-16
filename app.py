import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIG & BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    .stApp { background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important; color: white !important; }
    .title-text { background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem !important; font-weight: 800 !important; font-family: 'Arial Black', sans-serif !important; }
    
    /* Standard Button Style */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        height: 70px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }

    /* Hover State */
    div.stButton > button:hover {
        border: 1px solid #00ADEF !important;
        background: rgba(0, 173, 239, 0.1) !important;
    }

    /* SELECTED STATE: This keeps the button highlighted */
    .selected-btn div.stButton > button {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2) !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(142, 45, 226, 0.4) !important;
    }

    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: white !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
def check_password():
    if st.query_params.get("wake") == "true":
        st.write("Engine Warm.")
        st.stop()
    if "password_correct" not in st.session_state:
        st.markdown('<h1 class="title-text">Strategy Vault</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Consultant Access Code", type="password", key="pwd_input")
        if st.button("Unlock GESHIDO® Engine"):
            if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Invalid Access Code.")
        return False
    return True

if check_password():
    st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)
    
    # 3. STEP 1: MATURITY
    st.markdown('### Step 1: Diagnose Maturity')
    m_col1, m_col2, m_col3 = st.columns(3)
    
    with m_col1:
        # If 'Explorer' is selected, wrap the button in the 'selected-btn' div
        if st.session_state.get("maturity") == "Explorer":
            st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button("🔭 EXPLORER", key="btn_exp"): st.session_state.maturity = "Explorer"; st.rerun()
        if st.session_state.get("maturity") == "Explorer": st.markdown('</div>', unsafe_allow_html=True)

    with m_col2:
        if st.session_state.get("maturity") == "Scaler":
            st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button("🚀 SCALER", key="btn_sca"): st.session_state.maturity = "Scaler"; st.rerun()
        if st.session_state.get("maturity") == "Scaler": st.markdown('</div>', unsafe_allow_html=True)

    with m_col3:
        if st.session_state.get("maturity") == "Innovator":
            st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
        if st.button("🤖 INNOVATOR", key="btn_inn"): st.session_state.maturity = "Innovator"; st.rerun()
        if st.session_state.get("maturity") == "Innovator": st.markdown('</div>', unsafe_allow_html=True)

    # 4. STEP 2: INDUSTRY BUTTONS
    if "maturity" in st.session_state:
        st.markdown('### Step 2: Select Industry Segment')
        industries = {
            "Financial": "🏦 Financial Services",
            "Retail": "🛒 Retail & FMCG",
            "Telco": "📡 Telecommunications",
            "Public": "🏛️ Public Sector",
            "Mining": "⛏️ Mining & Energy"
        }
        i_cols = st.columns(5)
        
        for i, (key, label) in enumerate(industries.items()):
            with i_cols[i]:
                # Apply selected style if this industry is in session state
                if st.session_state.get("ind") == label:
                    st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
                if st.button(label, key=f"ind_{key}"): 
                    st.session_state.ind = label
                    st.rerun()
                if st.session_state.get("ind") == label:
                    st.markdown('</div>', unsafe_allow_html=True)

    # 5. STEP 3: GENERATE
    if "ind" in st.session_state:
        st.markdown(f"**Selected Strategy Path:** `{st.session_state.ind}` | `{st.session_state.maturity}`")
        frictions = st.text_area("Define top friction points:", placeholder="e.g. Manual data entry...")
        
        if st.button("⚡ ORCHESTRATE ROADMAP", type="primary"):
            try:
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(
                    f"IQ Business Strategist: Industry {st.session_state.ind}, Maturity {st.session_state.maturity}. Frictions: {frictions}. Create a 12-week GESHIDO roadmap."
                )
                st.markdown("---")
                st.markdown(response.text)
                st.download_button("Download Strategy Brief", response.text, file_name="IQ_Strategy.md")
            except Exception as e:
                st.error(f"Engine Error: {e}")
