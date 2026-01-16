import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # DYNAMIC DISCOVERY: Prevents the 404 by finding what your key supports
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Priority: flash-1.5 -> pro-1.5 -> fallback to first available
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        context = f"Industry: {ind} | Maturity: {maturity} | Friction: {frictions}"
        if user_feedback:
            context += f" | STRATEGY CHALLENGE: {user_feedback}"

        prompt = f"""
        {context}
        Role: Lead AI Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).

        OUTPUT STRUCTURE:
        1. AI REASONING (The 'Magic'):
           - Step 1: Pattern Recognition (Deconstruct the friction)
           - Step 2: Economic Modeling (LTV vs Intervention Cost math)
           - Step 3: Strategy Selection (Logic for the chosen path)
        
        2. STRATEGIC TENSIONS (Identify 3 core trade-offs):
           Wrap each in <div class='blindspot-card'>.
           Example: 'Proactive vs. Intrusive', 'Short-term ROI vs. Brand Trust'.

        3. DYNAMIC ROADMAP: 3 Phase Cards using <div class='phase-card'>...</div>.
           If user_feedback exists, start with 'ADAPTATION LOGIC' explaining what changed.

        4. IMPACT TABLE: ROI with 'Data Logic' footnotes for every projection.

        STRICT: No stars (**), no code blocks. Use <h3> for internal headers.
        """
        
        response = model.generate_content(prompt)
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
