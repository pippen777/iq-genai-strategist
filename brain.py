import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Automatic model discovery to prevent 404s
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        model = genai.GenerativeModel(target_model)
        
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: Industry: {ind} | Maturity: {maturity} | Friction: {frictions}

        TASK: Generate an Executive Roadmap using clean HTML classes.
        
        REQUIRED STRUCTURE:
        1. THE 'AHA' MOMENT: Wrap in <div class='aha-box'><p class='aha-text'>...</p></div>
        2. 12-WEEK ROADMAP: Wrap Month 1, 2, and 3 content each in <div class='phase-card'>...</div>
        3. IMPACT TABLE: A clean HTML table. Use <span class="target-state"> for Target column numbers.

        STRICT RULES:
        - DO NOT include markdown code blocks (```html).
        - DO NOT include <html> or <body> tags.
        - Use <h3> for Month titles inside the cards. No stars (**).
        """
        
        response = model.generate_content(prompt)
        # Surgical strip of markdown code wrappers
        clean_res = re.sub(r"```[a-z]*\n?|```", "", response.text).strip()
        return clean_res
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
