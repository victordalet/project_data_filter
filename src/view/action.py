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
    def apply_filter(key: str, filter_input, button):
        if "uploaded_data" in st.session_state:
            data = st.session_state["uploaded_data"]

            # Vérifier si la colonne 'name' existe dans le DataFrame
            if key in data.columns:
                # Créer un champ de texte pour filtrer les valeurs de la colonne 'name'

                # Bouton pour appliquer le filtre
                if button:
                    if filter_input:
                        # Appliquer le filtre
                        filtered_data = data[
                            data[key].str.contains(filter_input, case=False, na=False)
                        ]
                    else:
                        # Si aucun filtre, afficher les données non filtrées
                        filtered_data = data

                    # Afficher les données filtrées
                    st.write(filtered_data)
            else:
                st.write("The 'name' column is not present in the dataset.")
