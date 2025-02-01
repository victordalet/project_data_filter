from typing import Tuple, Optional
import pandas as pd
import streamlit as st
from src.struct.data_manager import DataManager


class Action:
    @staticmethod
    def check_upload_file(
        file_uploader: st.file_uploader,
    ) -> Optional[Tuple[str, pd.DataFrame]]:
        if file_uploader:
            for file in file_uploader:
                if file.name not in st.session_state.uploaded_files:
                    st.session_state.uploaded_files.append(file.name)
                    file_path = file.name
                    file_type = "student" if "student" in file_path else "item"
                    file_extension = file_path.split(".")[-1]
                    return file_type, DataManager().get_data(
                        f"data/{file_path}", file_extension
                    )
        return None

    @staticmethod
    def save_data(data: pd.DataFrame, file_name: str, file_format: str):
        """
        Sauvegarde les données dans un fichier au format spécifié.
        """
        if file_format == "csv":
            data.to_csv(file_name, index=False)
        elif file_format == "json":
            data.to_json(file_name, orient="records")
        elif file_format == "xml":
            data.to_xml(file_name, index=False)
        elif file_format == "yaml":
            with open(file_name, "w") as f:
                f.write(data.to_yaml())
        st.success(f"Data saved successfully as {file_name}!")

    @staticmethod
    def sort_data(data: pd.DataFrame, key: str, ascending: bool = True) -> pd.DataFrame:
        """
        Trie les dataset en fonction d'une clé.
        """
        if key in data.columns:
            return data.sort_values(by=key, ascending=ascending)
        st.warning(f"The column '{key}' is not present in the dataset.")
        return data

    @staticmethod
    def apply_filter(data: pd.DataFrame, filters: list[dict[str, str]]) -> pd.DataFrame:
        """
        Applique un filtre sur les données en fonction de plusieurs colonnes et valeurs.
        """
        filtered_data = data.copy()
        for filter in filters:
            column, value = filter["column"], filter["value"]
            if column in filtered_data.columns:
                filtered_data = filtered_data[
                    filtered_data[column]
                    .astype(str)
                    .str.contains(value, case=False, na=False)
                ]
            else:
                st.warning(f"The column '{column}' is not present in the dataset.")
        return filtered_data
