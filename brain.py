import google.generativeai as genai
import streamlit as st

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # 1. AUTO-DISCOVER MODEL
        # This prevents the 404 by finding exactly what your key supports
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Prioritize 1.5 Flash, then Pro, then whatever is first
        target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        
        model = genai.GenerativeModel(target_model)
        
        # 2. THE 10/10 EXECUTIVE PROMPT
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Industry: {ind} | Maturity: {maturity}.
        Friction: {frictions}

        TASK: Generate an Executive Dashboard using HTML.
        
        REQUIRED SECTIONS:
        1. THE 'AHA' MOMENT: One bold, visionary sentence wrapped in a blue callout box.
        2. 12-WEEK ROADMAP: 3 frosted-glass Phase Cards for Month 1 (Value), Month 2 (Scale), and Month 3 (Govern).
        3. GESHIDO IMPACT: A small table of 'Now' vs 'Target'.

        HTML SPECIFICATIONS:
        - Box: <div style="padding:25px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px;">
        - Cards: <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:12px; border-top:4px solid #F02FC2; margin-bottom:15px;">
        - Typography: Use <h3> for titles. Strictly NO stars (**).
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Engine Alignment Error: {str(e)}"
