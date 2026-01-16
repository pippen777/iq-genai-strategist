import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # 1. AUTHENTICATE & DISCOVER MODELS
        # This prevents the 404 by finding exactly what your key supports
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Priority: flash-1.5 -> pro-1.5 -> any available
        if not model_list:
            return "<div style='color:red;'>API Error: No generative models found for this key.</div>"
            
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        prompt = f"""
        Role: Senior AI Partner at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity}. Friction: {frictions}

        TASK: Generate an Executive Roadmap.
        - THE 'AHA' MOMENT: 1 visionary sentence in <div class='aha-box'><p class='aha-text'>...</p></div>
        - 3 PHASE CARDS: Month 1 (Value), Month 2 (Scale), Month 3 (Govern).
          Wrap each in <div class='phase-card'>...</div>
        - IMPACT TABLE: Use <span class='target-state'> for ROI numbers.
        
        STRICT: No stars (**), no code blocks, no html/body tags.
        """
        
        response = model.generate_content(prompt)
        
        # Surgical cleanup of markdown artifacts
        clean_res = re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
        return clean_res
        
    except Exception as e:
        return f"<div style='color:red;'>Engine Alignment Error: {str(e)}</div>"
