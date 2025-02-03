import streamlit as st

import pandas as pd

from src.view.FIlterComponent import FilterComponent


class HomeComponent:
    @staticmethod
    def create_table_component(data: pd.DataFrame):
        st.write(data)

    @staticmethod
    def create_home_component(title: str = "Data Filter"):
        st.title(title)
        file_uploader = st.file_uploader(
            "Upload a file",
            type=["csv", "json", "yaml", "xml"],
            accept_multiple_files=True,
        )
        FilterComponent.display_filter_bar()
        FilterComponent.create_save_component()
        return file_uploader
