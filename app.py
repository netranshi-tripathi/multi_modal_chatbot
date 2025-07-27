from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os
import uvicorn

# Load .env variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="LangServe Example with Gemma and TinyLlama",
    description="An example FastAPI app using LangServe with Gemma and TinyLlama models via Ollama.",
    version="1.0.0",
)

# Initialize models
gemma_model = Ollama(model="gemma:2b", temperature=0.8)
tinyllama_model = ChatOllama(model="tinyllama", temperature=0.8)

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic}")
prompt2 = ChatPromptTemplate.from_template("Write a poem about {topic}")

# Add routes
add_routes(app, prompt1 | gemma_model, path="/essay")
add_routes(app, prompt2 | tinyllama_model, path="/poem")

# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
