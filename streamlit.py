import app
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


st.title("Content Generator")
prompt = st.text_input("Enter your prompt:")
if st.button("Generate Content"):
    if prompt:
        try:
            response =app.content_creation(prompt)
            st.write("Generated Content:",response)
            st.write(response.choices[0].text.strip())
        except Exception as e:
            st.error("Hope you like thi ")
    
    else:
        st.warning("please enter a prompt")        
                





