🌾 KrishiMitra AI
AI Assistant for Farmers

KrishiMitra AI is an AI-powered agriculture assistant designed to help farmers get quick and reliable answers to farming-related questions in simple Hindi.

The system uses Retrieval-Augmented Generation (RAG) with a local Large Language Model (LLM) to generate answers based on an agriculture knowledge dataset.

KrishiMitra also supports voice-based interaction, allowing farmers to ask questions using their voice and listen to AI responses.

🚜 Key Features

🌱 Ask agriculture questions in Hindi

🎤 Voice-based input – Farmers can ask questions using speech

🔊 Speech output (Text-to-Speech) – AI reads answers aloud

🤖 AI-generated responses using local LLM (Mistral via Ollama)

🔎 Semantic search with FAISS vector database

📚 Agriculture knowledge dataset for accurate responses

💾 Chat history storage using SQLite

🌗 Light / Dark theme support

⚙️ Language and theme settings

🌐 Simple and farmer-friendly interface

🧠 How the AI Works

KrishiMitra follows a Retrieval-Augmented Generation (RAG) pipeline.

Farmer Question (Text / Voice)
           ↓
Speech-to-Text (Browser API)
           ↓
Sentence Transformer (Embeddings)
           ↓
FAISS Vector Search
           ↓
Relevant Agriculture Context
           ↓
Local LLM (Mistral via Ollama)
           ↓
Hindi AI Answer
           ↓
Text-to-Speech (Voice Response)

This approach ensures the AI answers using relevant agriculture knowledge instead of guessing.

🖥️ Application Screens
Login Page
<p align="center"> <img src="images/login-page.png" width="800"> </p>
Main Interface
<p align="center"> <img src="images/main-page.png" width="800"> </p>
AI Answer Generation
<p align="center"> <img src="images/search-ans.png" width="800"> </p>
Chat History
<p align="center"> <img src="images/history-stored.png" width="800"> </p>
Theme Support (Dark Mode)
<p align="center"> <img src="images/dark-mode.png" width="800"> </p>
Settings Panel
<p align="center"> <img src="images/settings-lang.png" width="800"> </p>
🏗️ Tech Stack
Backend

Python

FastAPI

AI / Machine Learning

Sentence Transformers

FAISS Vector Database

Ollama

Mistral LLM

Database

SQLite

Frontend

HTML

CSS

JavaScript

Voice Features

Browser Speech Recognition API (Voice Input)

Browser Text-to-Speech API (Voice Output)

📂 Project Structure
krishimitra-ai
│
├── app.py
├── database.py
├── rag_local_llm.py
├── embed_dataset_local.py
├── retrieve.py
│
├── krishimitra_full_dataset.json
├── krishi_index.faiss
│
├── index.html
├── main.html
│
├── images
│   ├── login-page.png
│   ├── main-page.png
│   ├── search-ans.png
│   ├── history-stored.png
│   ├── dark-mode.png
│   ├── settings-lang.png
│
├── README.md
└── requirements.txt
⚙️ Installation
Clone the repository
git clone https://github.com/yourusername/krishimitra-ai.git
cd krishimitra-ai
Install dependencies
pip install -r requirements.txt
Install Ollama

Download Ollama:

https://ollama.ai

Install the model:

ollama pull mistral
Generate vector embeddings
python embed_dataset_local.py

This creates the FAISS vector database used for semantic search.

Run the server
py -m uvicorn app:app --reload

Server runs at:

http://127.0.0.1:8000
🌾 Example Questions

Farmers can ask questions like:

गेहूं में पहली खाद कब डालें?
धान की रोपाई कब करें?
फसल में कीट लग जाए तो क्या करें?
टमाटर में फूल झड़ना कैसे रोकें?

KrishiMitra will generate answers and can read them aloud using speech output.

🎯 Future Improvements

📷 Crop disease detection using images
🌦 Weather information integration
💰 Real-time mandi price updates
📱 Mobile application for farmers
🌍 Multi-language support

If you want, I can also give you one more upgrade that will make this README look like a professional AI project on GitHub (with badges, architecture diagram, and project banner at the top).

this readme file 📂 Project Structure krishimitra-ai │ ├── app.py ├── database.py ├── rag_local_llm.py ├── embed_dataset_local.py ├── retrieve.py │ ├── krishimitra_full_dataset.json ├── krishi_index.faiss │ ├── index.html ├── main.html │ ├── images │ ├── login-page.png │ ├── main-page.png │ ├── search-ans.png │ ├── history-stored.png │ ├── dark-mode.png │ ├── settings-lang.png │ ├── README.md └── requirements.txt ⚙️ Installation Clone the repository git clone https://github.com/yourusername/krishimitra-ai.git cd krishimitra-ai Install dependencies pip install -r requirements.txt Install Ollama
did not leave a line here and many places fix this

The issue happens because GitHub Markdown needs blank lines between headings, text, and code blocks.
I fixed the formatting so everything renders correctly on GitHub.

You can copy-paste this corrected section directly.

📂 Project Structure
krishimitra-ai
│
├── app.py
├── database.py
├── rag_local_llm.py
├── embed_dataset_local.py
├── retrieve.py
│
├── krishimitra_full_dataset.json
├── krishi_index.faiss
│
├── index.html
├── main.html
│
├── images
│   ├── login-page.png
│   ├── main-page.png
│   ├── search-ans.png
│   ├── history-stored.png
│   ├── dark-mode.png
│   ├── settings-lang.png
│
├── README.md
└── requirements.txt
⚙️ Installation
Clone the repository
git clone https://github.com/yourusername/krishimitra-ai.git
cd krishimitra-ai
Install dependencies
pip install -r requirements.txt
Install Ollama

Download Ollama from:

https://ollama.ai

Then install the model:

ollama pull mistral
Generate vector embeddings
python embed_dataset_local.py

This creates the FAISS vector database used for semantic search.

Run the server
py -m uvicorn app:app --reload

Server will run at:

http://127.0.0.1:8000
🌾 Example Questions
गेहूं में पहली खाद कब डालें?
धान की रोपाई कब करें?
फसल में कीट लग जाए तो क्या करें?
टमाटर में फूल झड़ना कैसे रोकें?

💡 Tip:
Make sure every section in your README has a blank line before and after code blocks like this:

Text


code


Text

Otherwise GitHub merges them together.

If you want, I can also give you a fully polished README version with perfect spacing everywhere (the one you pasted earlier still has some hidden Markdown issues that will appear after pushing to GitHub).

give me full proper readme with proper lining and spacing 

Below is a fully formatted README.md with correct spacing, headings, and code blocks so it renders perfectly on GitHub.
You can copy-paste this directly.

🌾 KrishiMitra AI
AI Assistant for Farmers

KrishiMitra AI is an AI-powered agriculture assistant designed to help farmers get quick and reliable answers to farming-related questions in simple Hindi.

The system uses Retrieval-Augmented Generation (RAG) with a local Large Language Model (LLM) to generate answers based on an agriculture knowledge dataset.

KrishiMitra also supports voice-based interaction, allowing farmers to ask questions using their voice and listen to AI responses.

🚜 Key Features

🌱 Ask agriculture questions in Hindi

🎤 Voice-based input – Farmers can ask questions using speech

🔊 Speech output (Text-to-Speech) – AI reads answers aloud

🤖 AI-generated responses using local LLM (Mistral via Ollama)

🔎 Semantic search with FAISS vector database

📚 Agriculture knowledge dataset for accurate responses

💾 Chat history storage using SQLite

🌗 Light / Dark theme support

⚙️ Language and theme settings

🌐 Simple and farmer-friendly interface

🧠 How the AI Works

KrishiMitra follows a Retrieval-Augmented Generation (RAG) pipeline.

Farmer Question (Text / Voice)
           ↓
Speech-to-Text (Browser API)
           ↓
Sentence Transformer (Embeddings)
           ↓
FAISS Vector Search
           ↓
Relevant Agriculture Context
           ↓
Local LLM (Mistral via Ollama)
           ↓
Hindi AI Answer
           ↓
Text-to-Speech (Voice Response)

This ensures answers are context-based and relevant to agriculture knowledge.

🖥️ Application Screens
Login Page
<p align="center"> <img src="images/login-page.png" width="800"> </p>
Main Interface
<p align="center"> <img src="images/main-page.png" width="800"> </p>
AI Answer Generation
<p align="center"> <img src="images/search-ans.png" width="800"> </p>
Chat History
<p align="center"> <img src="images/history-stored.png" width="800"> </p>
Theme Support (Dark Mode)
<p align="center"> <img src="images/dark-mode.png" width="800"> </p>
Settings Panel
<p align="center"> <img src="images/settings-lang.png" width="800"> </p>
🏗️ Tech Stack
Backend

Python

FastAPI

AI / Machine Learning

Sentence Transformers

FAISS Vector Database

Ollama

Mistral LLM

Database

SQLite

Frontend

HTML

CSS

JavaScript

Voice Features

Browser Speech Recognition API (Voice Input)

Browser Text-to-Speech API (Voice Output)

📂 Project Structure
krishimitra-ai
│
├── app.py
├── database.py
├── rag_local_llm.py
├── embed_dataset_local.py
├── retrieve.py
│
├── krishimitra_full_dataset.json
├── krishi_index.faiss
│
├── index.html
├── main.html
│
├── images
│   ├── login-page.png
│   ├── main-page.png
│   ├── search-ans.png
│   ├── history-stored.png
│   ├── dark-mode.png
│   ├── settings-lang.png
│
├── README.md
└── requirements.txt
⚙️ Installation
Clone the repository
git clone https://github.com/yourusername/krishimitra-ai.git
cd krishimitra-ai
Install dependencies
pip install -r requirements.txt
Install Ollama

Download Ollama from:

https://ollama.ai

Install the model:

ollama pull mistral
Generate vector embeddings
python embed_dataset_local.py

This creates the FAISS vector database used for semantic search.

Run the server
py -m uvicorn app:app --reload

Server runs at:

http://127.0.0.1:8000
🌾 Example Questions

Farmers can ask questions like:

गेहूं में पहली खाद कब डालें?
धान की रोपाई कब करें?
फसल में कीट लग जाए तो क्या करें?
टमाटर में फूल झड़ना कैसे रोकें?

KrishiMitra will generate answers using the agriculture dataset and can read them aloud using speech output.

🎯 Future Improvements

📷 Crop disease detection using images

🌦 Weather information integration

📱 Mobile application for farmers
