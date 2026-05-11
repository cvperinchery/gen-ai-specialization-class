
# LangChain and Ollama imports
# from langchain_ollama import ChatOllama, OllamaEmbeddings
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_core.prompts import PromptTemplate
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_core.runnables import RunnableLambda
import textwrap
import os
from dotenv import load_dotenv

load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")
# if HF_TOKEN is None: 
#     raise ValueError("HF_TOKEN not found. Make sure it exists in the .env file.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None: 
    raise ValueError("OPENAI_API_KEY not found. Make sure it exists in the .env file.")

# from openai import OpenAI

# client = OpenAI()

# completion = client.chat.completions.create(
#                         model="gpt-3.5-turbo",
#                         messages=[\
#                             {"role": "system", "content": "You are a helpful HR assisstant."},
#                             {"role": "user", "content": "Hello!"}
#                             ])

# print(completion.choices[0].message.content)

import openai
def get_completion(prompt, model="gpt-3.5-turbo"): 
    messages = [{"role": "user", "content": prompt}] 
    response = openai.ChatCompletion.create( 
                model=model, 
                messages=messages, 
                temperature=0, ) 
    return response.choices[0].message["content"] 
print(get_completion("Your query"))

# # llm = ChatOpenAI(model="gpt4o-mini", temperature=0.2)

# '''
# RAG Architecture
# - Import Documents
# - Text Chunking
# - Embedding Generation
# - Vector Database (FAISS)
# - User Query
# - Similarity Search 
# - Relevent Context
# - LLM Answer


# '''

# # Load the PDF, split it into text chunks, embed using Ollama, and return a retriever object
# def create_vectors(report_name: str): # report_name is the path to the PDF file
#     loader = PyPDFLoader(report_name)
#     docs = loader.load()

#     # Split document into manageable text chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
#     chunks = text_splitter.split_documents(docs)

#     # Create vectorstore from embeddings
#     # embeddings = OllamaEmbeddings(model='bge-m3:latest')
#     # nomic-embed-text:latest is another good embedding model from Ollama, you can experiment with different models to see which one works best for your use case
#     embeddings = OllamaEmbeddings(model='nomic-embed-text')
#     vectorstore = FAISS.from_documents(chunks, embeddings)

#     # Return retriever object to fetch relevant context
#     retriever = vectorstore.as_retriever()
#     return retriever

# def main():

#     # Initialize any tools

#     # Create the agent
#     conversation_agent = create_react_agent(
#         model=llm,
#     )
#     print("AI Human Resources Assisstant")
#     user_question = input("How can I help you today? ")
#     result = conversation_agent.invoke({"messages": [("user", user_question)]})
#     print(result["messages"][-1].content)