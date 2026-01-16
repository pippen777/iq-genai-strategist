import google.generativeai as genai
import streamlit as st

def orchestrate_strategy(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Discovery logic to prevent 404
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
        model = genai.GenerativeModel(target)
        
        prompt = f"""
        System: IQ Business Senior Strategist. Methodology: GESHIDO®. 
        Input: {ind} sector, {maturity} maturity. Friction: {frictions}.
        Required Format (No stars **):
        [VISION] 1-sentence bold vision.
        [KPI] BEFORE vs AFTER metrics for the specific friction.
        [M1], [M2], [M3] 4 bullets each.
        """
        res = model.generate_content(prompt).text
        return res
    except Exception as e:
        return f"ERROR: {e}"

def extract_section(text, tag, end_tag=None):
    start = text.find(tag) + len(tag)
    end = text.find(end_tag) if end_tag else len(text)
    return text[start:end].replace("**", "").strip()
