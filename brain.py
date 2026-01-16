import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        context = f"Industry: {ind} | Maturity: {maturity} | Friction: {frictions}"
        if user_feedback:
            context += f" | USER CHALLENGE: {user_feedback}"

        prompt = f"""
        {context}
        Role: Lead AI Orchestrator at IQ Business. 
        Framework: GESHIDO®.

        OUTPUT STRUCTURE:
        1. AI THINKING PROCESS: 
           Step 1: Pattern Recognition (What did the AI find?)
           Step 2: Economic Modeling (LTV vs Intervention Cost math)
           Step 3: Strategy Selection (Why this specific GESHIDO path?)
        
        2. STRATEGIC TENSIONS (Identify 3 core trade-offs):
           Use <div class='blindspot-card'> for each. Label them 'Value vs Volume', 'Proactive vs Intrusive', etc.

        3. DYNAMIC ROADMAP: 3 Phase Cards using <div class='phase-card'>...</div>.
           If user_feedback is present, start with: "ADAPTING LOGIC: [List specific changes to timeline/reach/ROI]"

        4. IMPACT TABLE: ROI with 'Reasoning Notes' for every number.

        STRICT: No stars (**). No generic fluff. Show the 'Magic' in the logic.
        """
        
        response = model.generate_content(prompt)
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"Error: {str(e)}"
