import streamlit as st
import os
from io import BytesIO
from pypdf import PdfReader # Corrected import for pypdf

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings # For generating embeddings from OpenAI
from langchain_community.vectorstores import FAISS # For efficient similarity search
from langchain_openai import ChatOpenAI # For the OpenAI LLM (e.g., gpt-3.5-turbo)
from langchain.chains.Youtubeing import load_qa_chain# CORRECTED LINE HERE
from langchain.prompts import PromptTemplate

# --- Streamlit Page Configuration ---
st.set_page_config(layout="wide", page_title="PDF Q&A Assistant")
st.title("📄 AI-Powered PDF Q&A Assistant")

# --- Initialize OpenAI API Key ---
# Check if API key is in Streamlit secrets (for deployment)
if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# Check if API key is in environment variables (for local development)
elif os.getenv("OPENAI_API_KEY") is not None:
    pass # Already set from environment
else:
    # If not set, display a warning and a text input for the user
    st.warning("Please enter your OpenAI API Key to use the app.")
    st.info("You can get your API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)")
    openai_api_key_input = st.text_input("OpenAI API Key:", type="password")
    if openai_api_key_input:
        os.environ["OPENAI_API_KEY"] = openai_api_key_input
    else:
        st.stop() # Stop execution if key is not provided

# --- Function to process PDF and create knowledge base ---
@st.cache_resource # Cache the result to avoid re-processing on every rerun
def process_pdf(_uploaded_file):
    if _uploaded_file is not None:
        st.info("Processing PDF... This may take a moment.")
        try:
            # 1. Extract Text from PDF
            pdf_reader = PdfReader(BytesIO(_uploaded_file.read()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or "" # Handle pages with no extractable text

            # 2. Split Text into Chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text)

            # 3. Create Embeddings and Store in Vector DB
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.from_texts(chunks, embeddings)
            st.success("PDF processed and knowledge base created!")
            return vector_store
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
            st.stop()
    return None

# --- Custom Prompt for LLM (Optional, but good for RAG) ---
# This prompt instructs the LLM to use the provided context for answers
template = """
You are an AI assistant specialized in answering questions based on provided document context.
Answer the question only from the provided context. If the answer is not in the context,
state that you cannot find the answer in the provided document.
Do not make up information.

Context:
{context}

Question: {question}

Answer:
"""
QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)

# --- Streamlit UI for PDF Upload ---
uploaded_file = st.sidebar.file_uploader("Upload your PDF document", type="pdf")

vector_store = None
if uploaded_file:
    vector_store = process_pdf(uploaded_file)

# --- Streamlit UI for Question Asking ---
if vector_store:
    query = st.text_input("Ask a question about the PDF:", placeholder="e.g., What is the main topic of this document?")

    if query:
        # Show a spinner while processing
        with st.spinner("Searching for answers..."):
            try:
                # 1. Retrieve Relevant Chunks
                # Search the vector store for the most similar chunks to the query
                docs = vector_store.similarity_search(query, k=4) # k=4 retrieves 4 most relevant chunks

                # 2. Query the LLM
                # Use a specific LLM model, like gpt-3.5-turbo for chat
                llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7) # Adjust temperature for creativity/consistency
                chain = load_qa_chain(llm, chain_type="stuff", prompt=QA_CHAIN_PROMPT) # "stuff" puts all docs in one prompt
                response = chain.run(input_documents=docs, question=query)

                st.subheader("Answer:")
                st.write(response)
                st.markdown("---") # Separator
                st.info("Disclaimer: Answers are generated by an AI model based on the provided PDF content and may not always be 100% accurate.")

            except Exception as e:
                st.error(f"Error getting answer: {e}")
                if "authentication_error" in str(e) or "Incorrect API key" in str(e):
                    st.warning("Please ensure your OpenAI API Key is correctly set in Streamlit Secrets or provided in the text input.")
    else:
        st.info("Enter your question above to get started.")
else:
    st.info("Please upload a PDF document on the sidebar to enable the Q&A functionality.")