# 🌾 KrishiMitra AI

## AI Assistant for Farmers

KrishiMitra AI is an **AI-powered agriculture assistant** designed to help farmers get **quick and reliable answers to farming-related questions in simple Hindi**.

The system uses **Retrieval-Augmented Generation (RAG)** with a **local Large Language Model (LLM)** to generate answers using an agriculture knowledge dataset.

KrishiMitra also supports **voice interaction**, allowing farmers to **ask questions using speech and listen to spoken answers**.

---

# 🚜 Features

- 🌱 Ask agriculture questions in **Hindi**
- 🎤 **Voice-based input** using speech recognition
- 🔊 **Speech output (Text-to-Speech)** for listening to answers
- 🤖 AI-powered responses using **Mistral via Ollama**
- 🔎 **Semantic search using FAISS vector database**
- 📚 Custom **agriculture knowledge dataset**
- 💾 **Chat history storage** using SQLite
- 🌗 **Light and Dark mode interface**
- ⚙️ Language and interface settings
- 🌐 Simple **farmer-friendly UI**

---

# 🧠 How the AI Works

KrishiMitra follows a **Retrieval-Augmented Generation (RAG)** pipeline.

```
Farmer Question (Text / Voice)
        ↓
Speech-to-Text
        ↓
Sentence Transformer Embedding
        ↓
FAISS Vector Search
        ↓
Relevant Agriculture Context
        ↓
Local LLM (Mistral via Ollama)
        ↓
Hindi AI Answer
        ↓
Text-to-Speech Output
```

This ensures answers come from **relevant agricultural knowledge instead of guessing**.

---

# 🖥️ Demo

## Login Page

![Login Page](images/login-page.png)

Users enter their mobile number to access the system.

---

## Main Interface

![Main Interface](images/main-page.png)

Farmers can type or speak agriculture questions.

---

## AI Answer Generation

![AI Answer](images/search-ans.png)

The system retrieves relevant information from the dataset and generates an answer.

---

## Chat History

![History](images/history-stored.png)

Previous questions and answers are saved for reference.

---

## Dark Mode Interface

![Dark Mode](images/dark-mode.png)

Users can switch between **light and dark themes**.

---

## Settings Panel

![Settings](images/settings-lang.png)

Allows language and interface customization.

---

# 🏗 Technology Stack

### Backend

- Python
- FastAPI

### AI / Machine Learning

- Sentence Transformers
- FAISS Vector Database
- Ollama
- Mistral LLM

### Database

- SQLite

### Frontend

- HTML
- CSS
- JavaScript

### Voice Features

- Browser Speech Recognition API (Voice Input)
- Browser Text-to-Speech API (Voice Output)

---

# 📂 Project Structure

```
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
│   └── settings-lang.png
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Requirements

- Python **3.9 or higher**
- Ollama installed

---

# ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/yourusername/krishimitra-ai.git
```

### 2. Enter the project folder

```
cd krishimitra-ai
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install the AI model

```
ollama pull mistral
```

### 5. Generate embeddings

```
python embed_dataset_local.py
```

### 6. Run the backend server

```
py -m uvicorn app:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

---

# 🌾 Example Questions

- गेहूं में पहली खाद कब डालें?
- धान की रोपाई कब करें?
- फसल में कीट लग जाए तो क्या करें?
- टमाटर में फूल झड़ना कैसे रोकें?

KrishiMitra generates answers and **can read them aloud using speech output**.

---

# 🚀 Future Improvements

- 📷 Crop disease detection using images
- 🌦 Weather information integration
- 💰 Real-time mandi price updates
- 📱 Mobile application for farmers
- 🌍 Multi-language support