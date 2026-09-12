# 🔎 Q&A Bot with Google Search

A simple AI-powered **Q&A chatbot** built with **LangChain, LangGraph, Groq, Google Serper, and Streamlit**.

The bot can answer questions using an LLM and can use **Google Search** as a tool when up-to-date or external information is required.

## ✨ Features

* 🤖 AI-powered question answering
* 🔍 Google Search integration
* 🧠 Conversation memory using LangGraph
* ⚡ Fast inference with Groq
* 🎨 Simple Streamlit UI
* 🛠️ Agent-based architecture using LangChain
* 🌐 Can retrieve up-to-date information from Google

## 🏗️ Tech Stack

* **Python**
* **LangChain**
* **LangGraph**
* **Groq**
* **Google Serper API**
* **Streamlit**
* **python-dotenv**

## 📂 Project Structure

```text
Q&A-Bot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ How It Works

```text
User Question
      ↓
Streamlit UI
      ↓
LangChain Agent
      ↓
   ┌───────────────┐
   │               │
   ↓               ↓
Groq LLM      Google Search
   │               │
   └───────┬───────┘
           ↓
       Final Answer
           ↓
       Streamlit UI
```

The agent decides whether it can answer directly using the LLM or needs to use the Google Search tool.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### Get API Keys

You need:

* **Groq API Key** for the LLM
* **Serper API Key** for Google Search

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 Example Questions

Try asking:

```text
Who is the current CEO of OpenAI?
```

```text
What are the latest developments in AI?
```

```text
Who won the latest Cricket World Cup?
```

```text
What is LangGraph?
```

The agent can use Google Search when external or current information is needed.

## 🧠 Memory

The project uses LangGraph's `InMemorySaver` as a checkpointer.

```python
memory = InMemorySaver()

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are an agent who can search anything on Google.",
    checkpointer=memory
)
```

A `thread_id` is used to associate messages with a conversation:

```python
config = {
    "configurable": {
        "thread_id": "user-1"
    }
}
```

> **Note:** `InMemorySaver` stores memory only while the application process is running. Restarting the application will clear the stored conversation state.

## 📦 Requirements

Example `requirements.txt`:

```text
streamlit
python-dotenv
langchain
langgraph
langchain-groq
langchain-community
google-search-results
```

## 🔐 Security

* Keep API keys inside `.env`.
* Never push `.env` to GitHub.
* Add `.env` to `.gitignore`.
* Do not expose API keys in frontend code.

## 🚧 Future Improvements

* [ ] Add streaming responses
* [ ] Add chat history UI
* [ ] Add multiple conversation threads
* [ ] Improve search tool integration
* [ ] Add persistent database-backed memory
* [ ] Add source/citation display
* [ ] Deploy the application
* [ ] Add authentication

## 📄 License

This project is intended for learning and experimentation with **LangChain, LangGraph, LLM agents, and tool calling**.

---

### ⭐ If you found this project useful

Give the repository a star and feel free to experiment with the code!
