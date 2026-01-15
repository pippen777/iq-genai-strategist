import streamlit as st
from google import genai
import os

# 1. BRANDING & STYLING
st.set_page_config(page_title="IQ GenAI Strategy Orchestrator", page_icon="🧠", layout="wide")

def apply_iq_branding():
    st.markdown("""
    <style>
    /* Main Background and Global Text */
    .stApp { 
        background-color: #FFFFFF !important; 
    }
    
    /* Force headings and normal text to be Midnight Blue */
    h1, h2, h3, p, span, label { 
        color: #001965 !important; 
        font-family: 'Arial', sans-serif !important; 
    }

    /* Sidebar Styling: Midnight Blue background with White text */
    [data-testid="stSidebar"] {
        background-color: #001965 !important;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* Input Box Styling */
    .stTextArea textarea {
        background-color: #F0F2F6 !important;
        color: #001965 !important;
        border: 1px solid #001965 !important;
    }

    /* GESHIDO Green Button */
    .stButton>button {
        background-color: #3F9C35 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.5rem 2rem !important;
    }
    
    /* Fix for invisible Maturity Level dropdown text */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #001965 !important;
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
