import streamlit as st
from openai import OpenAI
import os
import hmac

# 1. BRANDING & STYLING (IQ Business Midnight Blue & Action Green)
st.set_page_config(page_title="IQ GenAI Strategy Orchestrator", page_icon="🚀", layout="wide")

def local_css(file_name):
    st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFFFFF; }}
    .stButton>button {{ background-color: #3F9C35; color: white; border-radius: 8px; border: none; font-weight: bold; }}
    .stSidebar {{ background-color: #001965; color: white; }}
    h1, h2, h3 {{ color: #001965; font-family: 'Arial', sans-serif; }}
    .stAlert {{ border-left: 5px solid #3F9C35; }}
    </style>
    """, unsafe_allow_html=True)

local_css(None)

# 2. PASSWORD GATE (GESHIDO Security)
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
    # 3. KNOWLEDGE BASE GROUNDING
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
        st.subheader("🛠️ Strategy Tuning")
        maturity = st.selectbox("Client Maturity Level", ["Explorer (Hype/Ambiguity)", "Scaler (PoC Limbo)", "Innovator (Agentic Future)"])
        industry = st.text_input("Industry", placeholder="e.g., Banking, Retail")
        
    st.title("🧠 GenAI Strategy Orchestrator")
    st.markdown(f"**Target:** {industry} | **Stage:** {maturity}")

    # 5. THE "DESIGN & BUILD" INTERFACE
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # System Prompt: The Senior Strategist "Brain"
    system_prompt = f"""
    You are a Senior AI Strategist at IQ Business. Your goal is to move clients from 'Aha' to scaled performance.
    
    GROUNDING DATA:
    {knowledge}
    
    INSTRUCTIONS:
    1. Use GESHIDO® logic: Focus on 'Value Weekly, Foundations Monthly'.
    2. Address the '{maturity}' maturity stage specifically.
    3. Include a 'Secure & Responsible AI' section (POPIA compliance).
    4. Structure your output as a 12-week Acceleration Roadmap.
    5. Speak with executive presence: pragmatic, commercial, and human-centric.
    """

    user_input = st.text_area("Describe the top 3 friction points or 'Value Pools' you want to target:", 
                              placeholder="e.g. 1. Legal document review speed, 2. Customer service agentic support...")

    if st.button("Orchestrate Strategy"):
        if not user_input:
            st.warning("Please define your friction points first.")
        else:
            with st.spinner("Applying GESHIDO® Logic..."):
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Industry: {industry}\nMaturity: {maturity}\nFriction Points: {user_input}"}
                ]
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    temperature=0.7
                )
                
                strategy = response.choices[0].message.content
                st.markdown("---")
                st.subheader("📈 Your GenAI Acceleration Roadmap")
                st.markdown(strategy)
                
                st.download_button("Download Strategy Brief", strategy, file_name="IQ_GenAI_Strategy.md")

    st.markdown("---")
    st.caption("Powered by the IQ Business GenAI Keys to Winning Operating System™")
