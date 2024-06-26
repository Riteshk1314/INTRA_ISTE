
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time
from dotenv import load_dotenv
import bs4
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()
from langchain_community.document_loaders import PyPDFDirectoryLoader
groq_api_key = "gsk_QYCTZ50DNaBGbF6hhtTZWGdyb3FYnCbu2GHh8KKa5kUz9NKbJ"
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os 
load_dotenv()
import streamlit as st
sentence = "I have a problem with my iphone that needs to be resolved asap!!', 'labels': ['urgent', 'phone', 'computer', 'not urgent', 'tablet'], 'scores': [0.504, 0.479, 0.013, 0.003, 0.002]"
llm = Groq(model="mixtral-8x7b-32768", api_key=groq_api_key)
from llama_index.core.llms import ChatMessage
messages = [
ChatMessage(
            role="system", content="you are an emotionally intelligent chat bot. sentence along with sentiments is given, give appropriate answer. Dont mention the sentiment in your response "
        ),
        ChatMessage(role="user", content=f"{sentence}")]
xyz = llm.chat(messages)
print(xyz)
st.title('Rakshak')
st.write(xyz)