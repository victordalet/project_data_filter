import pandas as pd
import streamlit as st

from src.struct.stats_manager import StatsManager
from src.view.action import Action


class App:
    file_uploader: st.file_uploader

    def __init__(self):
        self.title: str = "Data Filter"
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = []

    def create_home_component(self):
        self.file_uploader = st.file_uploader(
            "Upload a file",
            type=["csv", "json", "yaml", "xml"],
            accept_multiple_files=True,
        )

    @staticmethod
    def create_table_component(data: pd.DataFrame):
        st.write(data)

    @staticmethod
    def create_stats_component(data: pd.DataFrame):
        min = StatsManager.min(data, "age")
        max = StatsManager.max(data, "age")
        avg = StatsManager.average(data, "age")
        st.write(f"Min: {min}, Max: {max}, Avg: {round(avg,2)}")

    def run(self):
        st.title(self.title)
        self.create_home_component()
        data = Action.check_upload_file(self.file_uploader)
        if data:
            file_type, data = data
            self.create_table_component(data)
            self.create_stats_component(data)


if __name__ == "__main__":
    App().run()
