import streamlit as st
import os
from io import BytesIO
from pypdf import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings # For generating embeddings from OpenAI
from langchain_community.vectorstores import FAISS # For efficient similarity search
from langchain_openai import ChatOpenAI # For the OpenAI LLM (e.g., gpt-3.5-turbo)
from langchain.chains.Youtubeing import load_qa_chain
from langchain.prompts import PromptTemplate

# ... (rest of the code for the app) ...