import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        
        # Safety overrides to ensure industrial strategy analysis isn't flagged
        safety = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]
        
        model = genai.GenerativeModel(selected_model, safety_settings=safety)
        
        context = f"Industry: {ind} | Maturity: {maturity} | Friction: {frictions}"
        if user_feedback:
            context += f" | STRATEGIC PIVOT (ADAPT TO THIS): {user_feedback}"

        # THE REFINED INTELLIGENCE PROMPT
        prompt = f"""
        {context}
        Role: Senior AI Strategy Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        
        REQUIRED STRUCTURE:
        1. EXECUTIVE BRIEFING: 
           Wrap in <div class='executive-brief'>
           <h3>Executive Briefing</h3>
           <ul>
             <li><strong>The Core Unlock:</strong> [1 sentence on the primary AI lever]</li>
             <li><strong>The Value:</strong> [1 sentence on the projected ROI/Impact]</li>
             <li><strong>The Critical Risk:</strong> [1 sentence on the top Strategic Tension]</li>
           </ul>
           </div>

        2. AI REASONING ENGINE: 
           Wrap in <div class='aha-box'>
           <h3>Reasoning Engine</h3>
           <p>Step 1: Pattern Recognition</p>
           <p>Step 2: Economic Modeling (LTV vs Intervention Cost math)</p>
           <p>Step 3: Strategy Selection Logic</p>
           </div>

        3. STRATEGIC TENSIONS: 
           Identify 3 core trade-offs. Wrap each in <div class='blindspot-card'>.
           Example: 'Proactive Value vs. Discount Dilution'.

        4. GESHIDO ROADMAP: 
           3 Phase Cards using <div class='phase-card'>...</div>. 
           If a Pivot exists, list the 'Adaptation Logic' (what changed in ROI/Reach) at the start of Phase 1.

        5. IMPACT TABLE: 
           Use a standard HTML <table> with <thead> and <tbody>.
           Columns: Metric, Current State, Target State (AI Impact), Data Logic.
           Wrap Target State values in <span class='target-state'>...</span>.

        STRICT: No stars (**). No markdown code blocks. Use professional, clinical executive language.
        """
        
        response = model.generate_content(prompt)
        # Surgical cleanup of markdown artifacts to protect the UI
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Strategic Engine Error: {str(e)}</div>"
