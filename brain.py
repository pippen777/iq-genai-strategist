import google.generativeai as genai
import streamlit as st
import re
import time #

def run_orchestrator(ind, maturity, frictions, user_feedback=None):
    # Number of attempts before giving up
    max_retries = 3
    retry_delay = 5 # Start with a 5-second wait

    for attempt in range(max_retries):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
            model = genai.GenerativeModel(selected_model)
            
            context = f"Context: {ind} Industry, {maturity} Maturity. Problem: {frictions}."
            if user_feedback:
                context += f" USER CHALLENGE: {user_feedback}. Adapt the strategy to address this specifically."

            prompt = f"""
            {context}
            Role: Lead AI Partner at IQ Business. 
            Framework: GESHIDO® (Value Weekly, Foundations Monthly).
            [... rest of your existing prompt ...]
            """
            
            response = model.generate_content(prompt)
            return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()

        except Exception as e:
            # Check if it's a 429 Error
            if "429" in str(e) and attempt < max_retries - 1:
                st.warning(f"Engine is cooling down (Attempt {attempt+1}/{max_retries}). Retrying in {retry_delay}s...")
                time.sleep(retry_delay) #
                retry_delay *= 2 # Exponential backoff
                continue
            else:
                return f"<div style='color:red;'>Engine Error: {str(e)}</div>"
