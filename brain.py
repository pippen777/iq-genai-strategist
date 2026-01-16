import google.generativeai as genai
import streamlit as st

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        model = genai.GenerativeModel(target_model)
        
        # WE ARE NOW STRIPPING THE BOILERPLATE
        prompt = f"""
        Role: Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: {ind} | {maturity}. Friction: {frictions}

        TASK: Generate the INNER HTML for an Executive Dashboard.
        
        STRICT RULES:
        1. DO NOT include <html>, <head>, <body>, or <style> tags.
        2. Use ONLY <div> tags with inline styles for the cards.
        3. Use <h3> for headers. No stars (**).
        
        REQUIRED STRUCTURE:
        - AHA BOX: <div style="padding:25px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px;">
        - PHASE CARDS: <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:12px; border-top:4px solid #F02FC2; margin-bottom:15px;">
        - Month 1: VALUE | Month 2: SCALE | Month 3: GOVERN
        - IMPACT TABLE: A clean HTML table showing Now vs Target.
        """
        
        response = model.generate_content(prompt)
        # Clean the response to ensure no markdown code blocks are returned
        return response.text.replace("```html", "").replace("```", "").strip()
    except Exception as e:
        return f"Engine Error: {str(e)}"
