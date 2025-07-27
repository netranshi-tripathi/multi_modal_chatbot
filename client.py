import streamlit as st
import requests

def get_gemma_response(input_text):
    url = "http://localhost:8000/essay/invoke"
    response = requests.post(url, json={"input": {"topic": input_text}})
    return response.json()['output']

def get_tinyllama_response(input_text):
    url = "http://localhost:8000/poem/invoke"
    response = requests.post(url, json={"input": {"topic": input_text}})
    return response.json()['output']

st.title("LangChain Demo: Gemma for Essay, TinyLlama for Poem")

input_text = st.text_input("Enter a topic for your essay (Gemma):")
input_text1 = st.text_input("Enter a topic for your poem (TinyLlama):")

if input_text:
    st.subheader("Essay Output:")
    st.write(get_gemma_response(input_text))

if input_text1:
    st.subheader("Poem Output:")
    poem = get_tinyllama_response(input_text1)
    st.write(poem.get("content") if isinstance(poem, dict) and "content" in poem else poem)
