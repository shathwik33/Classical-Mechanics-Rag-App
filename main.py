import os
import fitz
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_dir = os.path.join(current_dir, "db", "chroma_book_db")
pdf_path = "classical-mechanics.pdf"


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_text = ""
    for page in doc:
        all_text += page.get_text()
    return all_text


with open("content.txt", "w") as file:
    file.write(extract_text_from_pdf(pdf_path))

loader = TextLoader("content.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-base-v2")
Chroma.from_documents(docs, embeddings, persist_directory=persistent_dir)
