import pandas as pd
import streamlit as st
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
        self.create_input_filter()

    @staticmethod
    def create_table_component(data: pd.DataFrame):
        st.write(data)

    @staticmethod
    def create_input_filter():
        filter_value_name = st.text_input("name")
        filter_value_quantity = st.text_input("quantity")
        filter_value_price = st.text_input("category")
        filter_value_category = st.text_input("price")

        button_name = st.button("name")
        button_quantity = st.button("quantity")
        button_category = st.button("category")
        button_price = st.button("price")

        Action.apply_filter("name", filter_value_name, button_name)
        Action.apply_filter("quantity", filter_value_quantity, button_quantity)
        Action.apply_filter("price", filter_value_price, button_price)
        Action.apply_filter("category", filter_value_category, button_category)

        # Vérifier si des données ont été téléchargées

    def run(self):
        st.title(self.title)
        self.create_home_component()

        # Charger les données du fichier téléchargé
        data = Action.check_upload_file(self.file_uploader)
        if data:
            file_type, data = data
            # Enregistrer les données dans la session pour un accès ultérieur
            st.session_state["uploaded_data"] = data

            # Afficher les données sous forme de tableau
            self.create_table_component(data)


if __name__ == "__main__":
    App().run()
