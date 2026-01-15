import streamlit as st
from google import genai
import os

# 1. PAGE CONFIG & MODERN BRANDING
st.set_page_config(page_title="IQ Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    /* Hide old sidebar for modern UX */
    [data-testid="stSidebar"] { display: none !important; }
    
    /* Midnight Dark Background */
    .stApp {
        background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important;
        color: white !important;
    }

    /* Gradient Title */
    .title-text {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        font-family: 'Arial Black', sans-serif !important;
        margin-bottom: 0px;
    }

    /* Step Subheaders */
    .step-header {
        color: rgba(255, 255, 255, 0.6);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.9rem;
        margin-top: 30px;
    }

    /* Modern Glassmorphism Inputs */
    .stTextArea textarea, .stTextInput input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
    }

    /* GESHIDO Action Button */
    .stButton>button {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2.5rem !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(142, 45, 226, 0.4);
    }

    /* Card styling for Maturity selection */
    div.stButton > button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        height: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. SECURE ACCESS GATE
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown('<h1 class="title-text">Strategy Vault</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Consultant Access Code", type="password")
        if st.button("Unlock GESHIDO® Engine"):
            if pwd == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Access Denied.")
        return False
    return True

if check_password():
    # 3. KNOWLEDGE BASE GROUNDING
    def load_iq_knowledge():
        try:
            with open("knowledge/iq_frameworks.txt", "r") as f:
                return f.read()
        except Exception:
            return "IQ Business Keys to Winning Framework and GESHIDO Philosophy."

    knowledge = load_iq_knowledge()

    # 4. THE ORCHESTRATION FLOW
    st.markdown('<p class="title-text">Orchestrator</p>', unsafe_allow_html=True)
    st.markdown('<p class="step-header">Step 1: Diagnose Maturity</p>', unsafe_allow_html=True)

    # Maturity Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔭 EXPLORER\n(Hype & Ambiguity)", key="exp"):
            st.session_state.maturity = "Explorer"
    with col2:
        if st.button("🚀 SCALER\n(PoC Limbo)", key="sca"):
            st.session_state.maturity = "Scaler"
    with col3:
        if st.button("🤖 INNOVATOR\n(Agentic Future)", key="inn"):
            st.session_state.maturity = "Innovator"

    # 5. STRATEGY INPUTS
    if "maturity" in st.session_state:
        st.markdown(f"**Diagnostic Result:** `{st.session_state.maturity.upper()}`")
        st.markdown('<p class="step-header">Step 2: Design Context</p>', unsafe_allow_html=True)
        
        industry = st.text_input("Industry Segment", placeholder="e.g. Retail, Financial Services")
        frictions = st.text_area("Identify the top 3 friction points or value pools:", height=150)

        # 6. GENERATION LOGIC (Gemini 2.0 Flash)
        if st.button("⚡ ORCHESTRATE ROADMAP"):
            if not frictions or not industry:
                st.warning("Please provide industry and friction context.")
            else:
                try:
                    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                    
                    system_instructions = f"""
                    You are a Senior AI Strategist at IQ Business. 
                    Grounding Knowledge: {knowledge}
                    
                    TASK: Generate a GenAI Acceleration Roadmap.
                    TONE: Executive, pragmatic, GESHIDO-aligned (Value Weekly, Foundations Monthly).
                    CONTEXT: Industry: {industry} | Maturity: {st.session_state.maturity}
                    FRICTIONS: {frictions}
                    
                    SECTIONS REQUIRED:
                    1. The 'Aha' Moment: Strategic Intent
                    2. 12-Week Roadmap: Divided into Month 1 (Value), Month 2 (Scale), Month 3 (Govern)
                    3. Secure & Responsible AI: POPIA and ethical guardrails.
                    4. GESHIDO Metrics: 3 OKRs to track success.
                    """

                    with st.spinner("Synthesizing IQ Strategy..."):
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=system_instructions
                        )
                        
                        st.markdown("---")
                        st.markdown('<p class="title-text" style="font-size: 2rem !important;">Acceleration Roadmap</p>', unsafe_allow_html=True)
                        st.markdown(response.text)
                        
                        st.download_button(
                            label="📥 Export Strategy Brief",
                            data=response.text,
                            file_name=f"IQ_Strategy_{industry}.md",
                            mime="text/markdown"
                        )
                except Exception as e:
                    st.error(f"Engine Error: {e}")

    # Branding Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("© 2026 iqbusiness | GenAI Keys to Winning Operating System™")
