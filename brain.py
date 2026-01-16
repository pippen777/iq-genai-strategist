import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        context = f"Strategic Context: {ind} Industry, {maturity} Maturity. Problem: {frictions}."
        if user_feedback:
            context += f" USER CHALLENGE: {user_feedback}. Adapt the strategy to address this."

        prompt = f"""
        {context}
        Role: Lead AI Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).

        REQUIRED HTML STRUCTURE (USE THESE EXACT CLASSES):
        1. REASONING: <div class='aha-box'><h3>Reasoning Engine</h3><p>[Math & Logic]</p></div>
        2. BLINDSPOT: <div class='blindspot-card'><strong>Strategic Blindspot:</strong> [Risk]</div>
        3. ROADMAP: 3 Phase Cards wrapped in <div class='phase-card'>...</div>
        4. IMPACT TABLE: Standard HTML table. Use <span class='target-state'>...</span> for Target column.

        STRICT: No stars (**), no code blocks. Use <h3> for titles inside cards.
        """
        
        response = model.generate_content(prompt)
        # Surgical cleanup of markdown artifacts
        clean_res = re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
        return clean_res
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
