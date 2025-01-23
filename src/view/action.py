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
