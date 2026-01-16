import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity}. Friction: {frictions}

        TASK: Generate an Executive Strategy Dashboard using ONLY clean HTML.
        
        RULES:
        1. THE 'AHA' MOMENT: 1 visionary sentence in <div class='aha-box'><p class='aha-text'>...</p></div>
        2. 3 PHASE CARDS: Use <div class='phase-card'> for each.
        3. IMPACT TABLE: Use <span class='target-state'> for the Target column.
        
        STRICT: Do NOT include ```html markdown or <html>/<body> tags. No stars (**).
        """
        
        response = model.generate_content(prompt)
        # Surgical strip of code wrappers
        return re.sub(r"```[a-z]*\n?|```", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
