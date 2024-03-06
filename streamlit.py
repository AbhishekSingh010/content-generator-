import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your content creation function from app
from app import content_creation

# Get Google API Key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Set title and input prompt
st.title("Content Generator")
prompt = st.text_input("Enter your prompt:")

# Function to display user input with chat icon
def user_message(message):
    st.markdown(f'<p style="background-color:#665975; padding: 10px; border-radius: 10px;"><b>User:</b> <span style="background: linear-gradient(to right, #66ff66, #009933); padding: 5px; border-radius: 5px; -webkit-background-clip: text; -webkit-text-fill-color: transparent; color: black;">{message}</span></p>', unsafe_allow_html=True)

# Function to display model response with bot icon
def bot_message(message):
    st.markdown(f'<p style="background-color:#6a8991; padding: 10px; border-radius: 10px;"><b>Bot:</b> <span style="; padding: 5px; border-radius: 5px; color: black;">{message}</span></p>', unsafe_allow_html=True)

# Generate content button
if st.button("Generate Content"):
    if prompt:
        try:
            # Get model response
            response = content_creation(prompt)
            user_message(prompt)
            bot_message(response.strip())  # Display the response directly
        except Exception as e:
            st.error("Error: " + str(e))
    else:
        st.warning("Please enter a prompt")
