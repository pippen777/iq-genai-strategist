import google.generativeai as genai
import streamlit as st

def orchestrate_strategy(ind, maturity, frictions):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # STABLE DISCOVERY: Prevents the 404/v1beta error
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        target = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        model = genai.GenerativeModel(target)
        
        prompt = f"""
        Role: IQ Business Lead Strategist. 
        Methodology: GESHIDO® (Foundations Monthly, Value Weekly).
        Input: {ind} sector, {maturity} maturity. Friction: {frictions}.
        
        Mandatory Dashboard Format (NO Markdown ** stars):
        [VISION] Bold 1-sentence executive vision.
        [KPI] Specific Before vs After impact for the friction provided.
        [M1], [M2], [M3] 12-week roadmap. Month 1 is Foundation. Month 3 is Agentic.
        """
        return model.generate_content(prompt).text
    except Exception as e:
        return f"ERROR: {e}"

def extract_section(text, tag, end_tag=None):
    try:
        start = text.find(tag) + len(tag)
        end = text.find(end_tag) if end_tag else len(text)
        return text[start:end].replace("**", "").strip()
    except: return "Content Synthesis Pending..."
