import google.generativeai as genai
import streamlit as st

def get_knowledge():
    try:
        with open("knowledge/iq_frameworks.txt", "r") as f:
            return f.read()
    except:
        return "IQ Business GESHIDO Framework: Value Weekly, Foundations Monthly."

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        knowledge = get_knowledge()
        
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity} Maturity.
        Friction: {frictions}

        TASK: Generate a high-impact dashboard using HTML/inline CSS for Streamlit markdown.
        
        REQUIREMENTS:
        1. THE 'AHA' MOMENT: A single sentence in a large, glowing blue callout box.
        2. 12-WEEK ROADMAP CARDS: Use 3 distinct HTML divs (Cards) for:
           - Month 1: VALUE (The Quick Win)
           - Month 2: SCALE (The Integration)
           - Month 3: GOVERN (The Foundation)
        3. GESHIDO METRICS: A clean table showing Before vs. After impact.

        STYLING:
        - Use border-radius: 15px, background: rgba(255,255,255,0.05), and border-top: 4px solid #00ADEF.
        - Avoid all stars (**). Use <h3> tags for headers.
        """
        return model.generate_content(prompt).text
    except Exception as e:
        return f"Engine Error: {e}"
