import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_dir = os.path.join(current_dir, "db", "chroma_book_db")

embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-base-v2")

db = Chroma(persist_directory=persistent_dir, embedding_function=embeddings)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

messages = [
    SystemMessage(content="You are a helpful assistant."),
]

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

while True:
    query = input("What questions do you have? ")
    relevant_docs = retriever.invoke(query)
    if query == "exit":
        break
    prompt = (
        "Here are some documents that might help answer the question: "
        + query
        + "\n\nRelevant Documents:\n"
        + "\n\n".join([doc.page_content for doc in relevant_docs])
        + "\n\nPlease provide an answer based only on the provided documents. If the answer is not found in the documents, respond with 'I'm not sure'."
    )
    messages.append(HumanMessage(content=prompt))
    results = model.invoke(messages)
    messages.append(AIMessage(results.content))
    print(results.content)
