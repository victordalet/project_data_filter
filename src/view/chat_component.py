import streamlit as st
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage


class ChatComponent:

    @staticmethod
    def display_chat(model: str):
        prompt = st.chat_input("Enter your question on your data")
        if prompt:
            st.write(f"You: {prompt}")
            st.write(f"Ollama: {ChatComponent.create_chat(model, prompt)}")

    @staticmethod
    def create_chat(model: str, messages: str) -> str:
        if "filtered_data" in st.session_state:
            data = st.session_state["filtered_data"]
        else:
            data = st.session_state.uploaded_data
        data_context = data.to_string()
        full_message = f"{messages}\n\nContext:\n{data_context}"
        llm = Ollama(model=model, request_timeout=120.0)
        messages = [ChatMessage(content=full_message)]
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        return response
