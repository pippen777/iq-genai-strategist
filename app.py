import streamlit as st
from google import genai
import os

# 1. BRANDING & STYLING
st.set_page_config(page_title="IQ GenAI Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    /* 1. The Main Background (Dark Midnight) */
    .stApp {
        background: radial-gradient(circle at top right, #1a1b3a, #0b101b) !important;
        color: white !important;
    }

    /* 2. Sidebar: Solid Midnight Blue */
    [data-testid="stSidebar"] {
        background-color: #001965 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* 3. The "Digital Integrator" Gradient Text */
    h1, .gradient-text {
        background: linear-gradient(to right, #00ADEF, #8E2DE2, #F02FC2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-family: 'Arial Black', sans-serif !important;
    }

    /* 4. Glassmorphism Input Boxes (Dark & Transparent) */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px);
    }

    /* 5. The GESHIDO® Button with Gradient Hover */
    .stButton>button {
        background: linear-gradient(45deg, #00ADEF, #F02FC2) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2.5rem !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(240, 47, 194, 0.3);
    }

    /* 6. Fixing invisible labels */
    label, p, span {
        color: rgba(255, 255, 255, 0.8) !important;
    }
    </style>
    """, unsafe_allow_html=True)

apply_iq_branding()

# 2. PASSWORD GATE
def check_password():
    if "password_correct" not in st.session_state:
        st.title("🔐 IQ Strategy Vault")
        password = st.text_input("Enter Access Code", type="password")
        if st.button("Access"):
            if password == st.secrets.get("APP_PASSWORD", "iq-vision-2026"):
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Invalid Code")
        return False
    return True

if check_password():
    # 3. KNOWLEDGE BASE LOADING
    def load_knowledge():
        try:
            with open("knowledge/iq_frameworks.txt", "r") as f:
                return f.read()
        except:
            return "IQ Business Keys to Winning Framework and GESHIDO Philosophy."

    knowledge = load_knowledge()

    # 4. SIDEBAR - THE "DIAGNOSE" PHASE
    with st.sidebar:
        st.image("https://iqbusiness.net/wp-content/uploads/2023/04/iqbusiness-logo-white.svg", width=200)
        st.markdown("---")
        maturity = st.selectbox("Maturity Level", ["Explorer (Hype/Ambiguity)", "Scaler (PoC Limbo)", "Innovator (Agentic Future)"])
        industry = st.text_input("Industry", placeholder="e.g., Banking")
        
    st.title("🧠 GenAI Strategy Orchestrator (Powered by Gemini)")

    # 5. THE "DESIGN & BUILD" INTERFACE
    # Initialize Gemini Client
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    system_prompt = f"""
    You are a Senior AI Strategist at IQ Business. Your goal is to move clients from 'Aha' to scaled performance.
    
    GROUNDING DATA:
    {knowledge}
    
    INSTRUCTIONS:
    1. Use GESHIDO® logic: Focus on 'Value Weekly, Foundations Monthly'.
    2. Address the '{maturity}' maturity stage specifically.
    3. Include a 'Secure & Responsible AI' section (POPIA compliance).
    4. Structure your output as a 12-week Acceleration Roadmap.
    """

    user_input = st.text_area("Describe the top 3 friction points or 'Value Pools' you want to target:", 
                              placeholder="e.g. 1. Speeding up credit risk assessments...")

    if st.button("Orchestrate Strategy"):
        if not user_input:
            st.warning("Please define your friction points.")
        else:
            with st.spinner("Gemini is applying GESHIDO® logic..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=f"{system_prompt}\n\nClient Input: {user_input}"
                )
                
                st.markdown("---")
                st.subheader("📈 Your GenAI Acceleration Roadmap")
                st.markdown(response.text)
                st.download_button("Download Strategy", response.text, file_name="IQ_Strategy.md")
