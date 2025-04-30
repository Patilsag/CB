from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API Key from environment variable
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Set up the prompt template for LangChain
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title('Langchain Demo with LLAMA2')
input_text = st.text_input("Search the topic you want")

# Ollama LLAMA2 LLM
llm = ollama(model="llama2")
output_parser = StrOutputParser()

# If user input is present, generate a response
if input_text:
    # Construct the prompt with the input question
    prompt_with_input = prompt.format(question=input_text)
    
    # Get the response from the LLAMA2 model
    response = llm.predict(prompt_with_input)

    # Parse the response (if necessary, based on your setup)
    parsed_response = output_parser.parse(response)

    # Display the response in Streamlit
    st.write(parsed_response)  # Display model output in Streamlit

else:
    st.write("Please enter a question to get started.")  # Show a prompt if no input is provided
