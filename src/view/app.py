import streamlit as st
from src.view.ChartComponent import ChartComponent
from src.view.HomeComponent import HomeComponent
from src.view.action import Action


class App:
    def __init__(self):
        self.file_uploader = None
        self.filter_history = []
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
            HomeComponent.create_table_component(data)
            ChartComponent.create_stats_component(data)


if __name__ == "__main__":
    App().run()
