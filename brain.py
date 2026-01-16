import google.generativeai as genai
import streamlit as st
import re

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        model = genai.GenerativeModel(target_model)
        
        prompt = f"""
        System: You are a Senior AI Strategist at IQ Business. 
        Framework: GESHIDO® (Value Weekly, Foundations Monthly).
        Context: Industry: {ind} | Maturity: {maturity} | Friction: {frictions}

        TASK: Generate a 12-week roadmap as a set of HTML Cards. 
        
        STYLING REQUIREMENTS:
        - Box: <div style="padding:25px; background:rgba(0,173,239,0.1); border-left:5px solid #00ADEF; border-radius:15px; margin-bottom:30px;">
        - Cards: <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:12px; border-top:4px solid #F02FC2; margin-bottom:15px;">
        
        STRICT RULES:
        1. DO NOT include <html>, <head>, or <body> tags. 
        2. DO NOT use markdown code blocks (```).
        3. Provide ONLY the <div> containers and the table.
        4. Use <h3> for titles. No stars (**).
        """
        
        response = model.generate_content(prompt)
        raw_text = response.text
        
        # CLEANUP: Remove common AI wrappers
        clean_res = re.sub(r"```html|```", "", raw_text) # Strip backticks
        clean_res = re.sub(r"<!DOCTYPE.*?>", "", clean_res, flags=re.DOTALL) # Strip DOCTYPE
        clean_res = re.sub(r"<html.*?>|</html>", "", clean_res, flags=re.DOTALL) # Strip html tags
        clean_res = re.sub(r"<head.*?>.*?</head>", "", clean_res, flags=re.DOTALL) # Strip head/style
        clean_res = re.sub(r"<body.*?>|</body>", "", clean_res, flags=re.DOTALL) # Strip body tags
        
        return clean_res.strip()
    except Exception as e:
        return f"Engine Alignment Error: {str(e)}"
