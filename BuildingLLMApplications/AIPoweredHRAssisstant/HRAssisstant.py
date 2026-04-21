from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
# from langchain_core.runnables import RunnableLambda
import textwrap

llm = ChatOpenAI(model="gpt4o-mini", temperature=0.2)

'''
RAG Architecture
- Import Documents
- Text Chunking
- Embedding Generation
- Vector Database (FAISS)
- User Query
- Similarity Search 
- Relevent Context
- LLM Answer


'''