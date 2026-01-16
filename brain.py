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
        Role: Lead AI Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity}. Friction: {frictions}

        TASK: Generate an Executive Strategy Dashboard.
        
        1. THE 'AHA' MOMENT: One visionary, aggressive sentence. 
           Wrap in: <div class='aha-box'><p class='aha-text'>YOUR_SENTENCE</p></div>
        
        2. 12-WEEK ROADMAP: 3 Phase Cards for Month 1 (Value), Month 2 (Scale), Month 3 (Govern).
           - Month 3 MUST include POPIA Compliance and Data Ethics.
        
        3. IMPACT TABLE: A Now vs Target table. Use <span class='target-state'> for targets.
        
        STRICT RULES:
        - No stars (**). Use <h3> for titles.
        - Ensure Month 1 has a 'Week 1' Quick Win.
        """
        
        response = model.generate_content(prompt)
        clean_res = re.sub(r"```[a-z]*\n?", "", response.text).replace("```", "").strip()
        return clean_res
    except Exception as e:
        return f'<div style="color:red;">Engine Alignment Error: {str(e)}</div>'
