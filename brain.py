import google.generativeai as genai
import streamlit as st

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity} Maturity.
        Friction: {frictions}

        TASK: Generate an Executive Dashboard using HTML.
        
        FORMATTING RULES:
        - Wrap the 'Aha' Moment in a <div style="padding:30px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px;">
        - Create 3 Phase Cards using <div style="background:rgba(255,255,255,0.05); padding:25px; border-radius:15px; border-top:4px solid #8E2DE2; margin:10px;">
        - Month 1: VALUE | Month 2: SCALE | Month 3: GOVERN
        - Use <h3> for headers. No stars (**).
        """
        return model.generate_content(prompt).text
    except Exception as e:
        return f"Engine Error: {e}"
