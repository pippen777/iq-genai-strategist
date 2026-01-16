import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        prompt = f"""
        Role: Lead AI Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Target: CEO/CTO level. Context: {ind} | {maturity}. Friction: {frictions}

        TASK: Generate an Executive Roadmap.
        1. THE 'AHA' MOMENT: 1 visionary, oversized claim. 
           Format: <div class='aha-box'><p class='aha-text'>...</p></div>
        2. PHASE CARDS: Month 1 (Value), Month 2 (Scale), Month 3 (Govern).
           Format: <div class='phase-card'><h3>PHASE TITLE</h3><ul>...</ul></div>
        3. IMPACT TABLE: Use <span class='target-state'> for ROI numbers.

        STRICT RULES:
        - NO markdown stars (**) or code blocks.
        - Month 1 MUST have a 'Week 1' Quick Win to prove ROI instantly.
        - Month 3 MUST include 'POPIA & ESG Compliance'.
        """
        
        response = model.generate_content(prompt)
        # Stripping all markdown artifacts
        clean_res = re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
        return clean_res
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
