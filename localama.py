
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

### Prompt Template

prompt =ChatPromptTemplate.from_messages(

    [
        ("system", "You are a helpful assistant. please response to the user queries"),
        ("user","Question:{question}")
    ]
)

### Streamlit Framework

st.title('Langchain demo with llama2')
input_text = st.text_input("Search the topic you want")

### Ollama LLAMA2 LLM

llm=ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
