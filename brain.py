import google.generativeai as genai
import streamlit as st

def run_orchestrator(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Discovery prevents 404
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        model = genai.GenerativeModel(target)
        
        prompt = f"""
        System: IQ Business Senior Strategist. Methodology: GESHIDO®. 
        Input: {ind} sector, {maturity} maturity. Friction: {frictions}.
        Required Format (No stars **):
        [VISION] 1-sentence visionary state.
        [KPI] Before vs After metrics strictly for the friction.
        [M1], [M2], [M3] 4 bullets each for Phase 1, 2, and 3.
        """
        return model.generate_content(prompt).text
    except Exception as e:
        return f"ERROR: {e}"

def clean_extract(text, tag, end_tag=None):
    start = text.find(tag) + len(tag)
    end = text.find(end_tag) if end_tag else len(text)
    return text[start:end].replace("**", "").strip()
