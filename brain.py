import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # 1. AUTO-DISCOVER MODEL
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Dynamically select the best available model to avoid 404
        target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        
        model = genai.GenerativeModel(target_model)
        
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity}. Friction: {frictions}

        TASK: Generate a 12-week roadmap using HTML Cards.
        
        STRUCTURE:
        1. THE 'AHA' MOMENT: 1 bold sentence in a blue callout box.
        2. PHASE CARDS: Month 1 (Value), Month 2 (Scale), Month 3 (Govern). 
           - Include 'POPIA Compliance' in Month 3.
        3. IMPACT TABLE: Use <span class="target-state"> for the Target column values.

        HTML RULES:
        - Aha Box: <div style="padding:25px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px; color:#00ADEF;">
        - Cards: <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:12px; border-top:4px solid #F02FC2; margin-bottom:15px; color:white;">
        - NO <html>/<body> tags. NO stars (**). Use <h3> for headers.
        """
        
        response = model.generate_content(prompt)
        # Clean markdown code blocks and return raw HTML
        clean_res = re.sub(r"```[a-z]*\n?", "", response.text).replace("```", "").strip()
        return clean_res
    except Exception as e:
        return f'<div style="color:red; padding:20px;">Engine Alignment Error: {str(e)}</div>'
