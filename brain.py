import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        
        # ADDED: Safety settings to prevent "Finish Reason 1" blocks
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        model = genai.GenerativeModel(selected_model, safety_settings=safety_settings)
        
        context = f"Industry: {ind} | Maturity: {maturity} | Friction: {frictions}"
        if user_feedback:
            context += f" | STRATEGIC PIVOT: {user_feedback}"

        prompt = f"""
        {context}
        Role: Senior AI Strategy Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).

        OUTPUT STRUCTURE:
        1. AI REASONING ENGINE (Show the 'Magic'):
           - Step 1: Pattern Recognition
           - Step 2: Economic Modeling (LTV vs Intervention Cost)
           - Step 3: Strategy Selection Logic
        
        2. 3 STRATEGIC TENSIONS: Wrap in <div class='blindspot-card'>.
        
        3. DYNAMIC ROADMAP: 3 Phase Cards using <div class='phase-card'>...</div>.
        
        4. IMPACT TABLE: ROI metrics with 'Data Logic' footnotes.

        STRICT: No stars (**), no code blocks. Use professional executive language.
        """
        
        response = model.generate_content(prompt)
        
        # ADDED: Defensive check for empty responses
        if not response.candidates or not response.candidates[0].content.parts:
            return "<div style='color:orange;'>The Strategy Engine was filtered. Retrying with a more clinical prompt...</div>"
            
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
        
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
