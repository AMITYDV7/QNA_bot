import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

st.title("LangChain Q&A")
st.markdown("# Simple Q&A Application")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

query = st.chat_input("Enter your question")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            res = llm.invoke(query)
            st.write(res.content)
            st.session_state.messages.append({"role": "ai", "content": res.content})