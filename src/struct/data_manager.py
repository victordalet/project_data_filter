from typing import Optional

import pandas as pd

from src.struct.structur_def import Student, Item


class DataManager:

    @staticmethod
    def get_csv_data(file_path: str) -> Optional[pd.DataFrame]:
        return pd.DataFrame(pd.read_csv(file_path))
