import os

import streamlit as st

from src.struct.data_manager import DataManager
from src.view.ChartComponent import ChartComponent
from src.view.HomeComponent import HomeComponent
from src.view.ChatComponent import ChatComponent
from src.view.action import Action


class App:
    def __init__(self):
        self.filter_bar = None
        self.file_uploader = None
        st.session_state["filter_history"] = []
        self.initialize_session_state()

    @staticmethod
    def initialize_session_state():
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = []

    def run(self):
        self.file_uploader = HomeComponent.create_home_component()
        data = Action.check_upload_file(self.file_uploader)
        if data:
            file_type, data = data
            st.session_state.uploaded_data = data
            HomeComponent.create_table_component(data)
            ChartComponent.create_stats_component(data)
        if os.getenv("ACTIVE_CHAT_BOT") == "True":
            ChatComponent.display_chat("llama3.1:8b")


if __name__ == "__main__":
    App().run()
