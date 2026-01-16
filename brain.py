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

        TASK: Generate a 12-week roadmap using HTML Cards for a Streamlit dashboard.
        
        STRUCTURE:
        1. THE 'AHA' MOMENT: One bold sentence in a blue callout.
        2. PHASE CARDS: Month 1 (Value), Month 2 (Scale), Month 3 (Govern).
        3. IMPACT TABLE: A clean Now vs Target table.

        STRICT STYLING (Inline CSS):
        - Aha Box: <div style="padding:25px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px; color:white;">
        - Phase Cards: <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:12px; border-top:4px solid #F02FC2; margin-bottom:15px; color:white;">
        
        RULES:
        - DO NOT use markdown code blocks (no backticks ```).
        - DO NOT include <html> or <body> tags.
        - Use <h3> for titles. No stars (**).
        """
        
        response = model.generate_content(prompt)
        text = response.text
        
        # SURGICAL CLEANUP: Strips backticks and language identifiers
        clean_res = re.sub(r"```[a-z]*\n?", "", text) 
        clean_res = clean_res.replace("```", "").strip()
        
        return clean_res
    except Exception as e:
        return f'<div style="color:red;">Engine Error: {str(e)}</div>'
