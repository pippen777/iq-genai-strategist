import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        model = genai.GenerativeModel(target_model)
        
        prompt = f"""
        System: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: Industry: {ind} | Maturity: {maturity} | Friction: {frictions}

        TASK: Generate a 12-week roadmap using HTML Cards.
        
        REQUIRED HTML STRUCTURE:
        1. THE 'AHA' MOMENT: <div class='aha-box'><p class='aha-text'>[Visionary Sentence]</p></div>
        2. PHASE CARDS: 3 cards for Month 1 (Value), Month 2 (Scale), Month 3 (Govern).
           Wrap each in: <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:12px; border-top:4px solid #F02FC2; margin-bottom:15px; color:white;">
        3. IMPACT TABLE: A clean HTML table. Use <span class="target-state"> for the Target State values.

        RULES:
        - Use ONLY <div> containers. NO <html> or <body>.
        - NO markdown stars (**). Use <h3> for titles.
        - Month 3 MUST include 'POPIA & Model Governance'.
        """
        
        response = model.generate_content(prompt)
        # Clean up markdown code blocks if the AI adds them
        clean_res = re.sub(r"```[a-z]*\n?", "", response.text).replace("```", "").strip()
        return clean_res
    except Exception as e:
        return f"<div style='color:red;'>Engine Error: {str(e)}</div>"
