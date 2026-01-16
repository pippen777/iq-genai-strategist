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

        TASK: Generate a 12-week roadmap using HTML Cards.
        
        STRUCTURE:
        1. THE 'AHA' MOMENT: 1 bold sentence in a <div style="padding:25px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px; color:#00ADEF;">
        2. PHASE CARDS: Month 1 (Value), Month 2 (Scale), Month 3 (Govern). 
           - Include a Month 3 card for 'Responsible AI & POPIA Compliance'.
        3. IMPACT TABLE: Use <span class="target-glow"> for the Target column values.

        RULES:
        - Use ONLY <div> containers. No <html> or <body> tags.
        - NO markdown stars (**). Use <h3> for headers.
        """
        
        response = model.generate_content(prompt)
        # Clean markdown code blocks
        clean_res = re.sub(r"```[a-z]*\n?", "", response.text).replace("```", "").strip()
        # Inject the glow class for the target values
        clean_res = clean_res.replace("target-glow", "target-state")
        
        return clean_res
    except Exception as e:
        return f'<div style="color:red;">Engine Alignment Error: {str(e)}</div>'
