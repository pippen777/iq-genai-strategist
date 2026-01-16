import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        # This context handles the "Pivot" conversation
        context = f"Context: {ind} Industry, {maturity} Maturity. Problem: {frictions}."
        if user_feedback:
            context += f" USER CHALLENGE: {user_feedback}. Adapt the strategy to address this specifically."

        prompt = f"""
        {context}
        Role: Lead AI Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).

        OUTPUT STRUCTURE:
        1. STRATEGIC REASONING: <div class='aha-box'><h3>Reasoning Engine</h3><p>Explain the 'Why' and the 'Math' behind your ROI numbers.</p></div>
        2. BLINDSPOT: <div style='border:1px solid #F02FC2; padding:15px; border-radius:10px;'><strong>Strategic Blindspot:</strong> [Identify a non-obvious risk]</div>
        3. ROADMAP: 3 Phase Cards (Month 1, 2, 3) in <div class='phase-card'>...</div>
        4. IMPACT TABLE: ROI metrics using <span class='target-state'>...</span>

        STRICT: No stars (**), no code blocks. Ground your numbers in industry benchmarks.
        """
        
        response = model.generate_content(prompt)
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Engine Error: {str(e)}</div>"
