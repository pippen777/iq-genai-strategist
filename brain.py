import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        context = f"Industry: {ind} | Maturity: {maturity} | Friction: {frictions}"
        if user_feedback:
            context += f" | PIVOT CHALLENGE: {user_feedback}"

        prompt = f"""
        {context}
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO®.

        SPECIAL ROI INSTRUCTION:
        - If Maturity is EXPLORER: Focus ROI on 'Cost of Inaction' and 'Opportunity Capture'.
        - If Maturity is SCALER: Focus ROI on 'Operational Efficiency' and 'Scale Multipliers'.

        REQUIRED OUTPUT:
        1. REASONING ENGINE: <div class='aha-box'><h3>Reasoning Engine</h3>...</div>. Explain the math.
        2. 3 TENSIONS: Use <div class='blindspot-card'>...</div>.
        3. ROADMAP: 3 Phase Cards using <div class='phase-card'>...</div>.
        4. IMPACT TABLE: ROI metrics using <span class='target-state'>...</span> with Data Logic footnotes.
           - You MUST use a standard <table> with <thead> and <tbody>.
           - Column 1: Metric | Column 2: Current State | Column 3: Target State (AI Impact) | Column 4: Data Logic.
           - Wrap the 'Target State' values in <span class='target-state'>...</span>.
           - Ensure every <tr> and <td> tag is explicitly closed.

        STRICT: No stars (**). Ensure the 'Orchestrator' vibe is professional and high-fidelity.
        """
        
        response = model.generate_content(prompt)
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"Error: {str(e)}"
