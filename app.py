import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

def content_creation(topic):
    tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}")
    # Get the Google API key from environment variables
    google_api_key = os.getenv('GOOGLE_API_KEY')

    # Check if the Google API key is available
    if google_api_key is None:
        raise ValueError("Google API key not found in environment variables")

    # Initialize ChatGoogleGenerativeAI with Gemini Pro model and Google API key
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

    # Initialize LLMChain with the ChatGoogleGenerativeAI instance and tweet prompt
    tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

    # Run the LLMChain to generate content
    response = tweet_chain.run(topic=topic)
    return response

