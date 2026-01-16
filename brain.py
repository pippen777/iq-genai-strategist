import google.generativeai as genai
import streamlit as st

def get_knowledge():
    """Restores the Knowledge Base Grounding"""
    try:
        with open("knowledge/iq_frameworks.txt", "r") as f:
            return f.read()
    except:
        return "IQ Business GESHIDO Framework: Value Weekly, Foundations Monthly."

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        knowledge = get_knowledge()
        
        # Discovery prevents 404
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        model = genai.GenerativeModel(target)
        
        prompt = f"""
        System: Senior AI Strategist at IQ Business. Grounding: {knowledge}
        Context: Industry {ind} | Maturity {maturity}.
        Friction: {frictions}
        
        Task: 12-Week Roadmap divided into:
        Month 1 (Value), Month 2 (Scale), Month 3 (Govern).
        Alignment: GESHIDO Philosophy.
        Format: Strictly clean text (no stars **).
        """
        return model.generate_content(prompt).text
    except Exception as e:
        return f"Engine Error: {e}"
