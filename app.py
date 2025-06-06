{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b6a9d61d-0e43-4327-91a9-68687eb3116d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'langchain'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 5\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mpypdf\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m PdfReader\n\u001b[1;32m----> 5\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mtext_splitter\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m RecursiveCharacterTextSplitter\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain_google_genai\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m GoogleGenerativeAIEmbeddings\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain_community\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mvectorstores\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m FAISS\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'langchain'"
     ]
    }
   ],
   "source": [
    "# app.py\n",
    "\n",
    "import streamlit as st\n",
    "from pypdf import PdfReader\n",
    "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
    "from langchain_google_genai import GoogleGenerativeAIEmbeddings\n",
    "from langchain_community.vectorstores import FAISS\n",
    "from langchain_google_genai import ChatGoogleGenerativeAI\n",
    "from langchain.chains.Youtubeing import load_qa_chain\n",
    "from langchain.prompts import PromptTemplate\n",
    "import os\n",
    "\n",
    "# --- Configuration ---\n",
    "# Load the Google API key from Streamlit's secrets\n",
    "# This is more secure than hardcoding or environment variables directly in production\n",
    "try:\n",
    "    os.environ[\"AIzaSyBZny4UJZB3XGdCpAYYHoaDc09dMDDqnzs\"] = st.secrets[\"AIzaSyBZny4UJZB3XGdCpAYYHoaDc09dMDDqnzs\"]\n",
    "]\n",
    "except KeyError:\n",
    "    st.error(\"Google API Key not found in .streamlit/secrets.toml. Please add it.\")\n",
    "    st.stop() # Stop the app if the key is missing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58d7f510-af4f-4c53-bf0e-298e49729e26",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
