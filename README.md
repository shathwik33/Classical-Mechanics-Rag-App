Sure! Here's the full content of the `README.md` file in one go — just copy and paste it:

# Classical Mechanics RAG App

A Retrieval-Augmented Generation (RAG) application that answers questions from classical mechanics using local PDFs and a vector database. This app processes a PDF, stores the content using vector embeddings, and uses a language model to answer questions interactively.

---

## 📌 Features

- Extracts text from `classical-mechanics.pdf`
- Splits and embeds text into vector database using ChromaDB
- Uses HuggingFace's `intfloat/e5-base-v2` embedding model
- Retrieves relevant content based on semantic similarity
- Generates answers using Gemini 2.0 Flash (Google Generative AI)
- Interactive Q&A session in the terminal

---

## 🧠 How It Works

1. **Extract text** from the provided PDF
2. **Split** the text into chunks using a text splitter
3. **Embed** the chunks and store in a local ChromaDB
4. **Retrieve** relevant chunks based on user query
5. **Answer** the question using a generative language model

---

## 📁 Project Structure

```
Classical-Mechanics-Rag-App/
├── classical-mechanics.pdf     # Source PDF
├── content.txt                 # Extracted text
├── main.py                     # Embeds and stores content
├── query.py                    # Interactive Q&A logic
├── db/                         # Local vector DB storage
└── .env                        # Environment file (API keys)
```

---

## 🛠 Requirements

Make a file called `requirements.txt` and add the following:

```
langchain
langchain-community
langchain-core
langchain-chroma
langchain-huggingface
langchain-google-genai
python-dotenv
chromadb
PyMuPDF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup Instructions

1. Clone the repo and navigate into it:

```bash
git clone https://github.com/shathwik33/Classical-Mechanics-Rag-App
cd Classical-Mechanics-Rag-App
```

2. Add your PDF file (`classical-mechanics.pdf`) to the root of the project.

3. Create a `.env` file and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## 🚀 Run the App

### Step 1: Extract, embed, and store documents

```bash
python main.py
```

### Step 2: Start asking questions

```bash
python query.py
```

Type your question and hit Enter. Type `exit` to quit the session.

---

## 🧪 Example Interaction

```
What questions do you have? What is Newton's second law?
F = ma, where F is the net force, m is mass, and a is acceleration.
```

---

## 🙌 Built With

- [LangChain](https://github.com/langchain-ai/langchain)
- [ChromaDB](https://www.trychroma.com/)
- [HuggingFace Transformers](https://huggingface.co/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
