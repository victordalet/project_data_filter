import pandas as pd


class FilterManager:
    @staticmethod
    def contains(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key].astype(str).str.contains(value, na=False)]

    @staticmethod
    def equals(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key] == value]

    @staticmethod
    def start_with(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key].astype(str).str.startswith(value)]

    @staticmethod
    def finish_with(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key].astype(str).endswith(value)]

    @staticmethod
    def is_below(data: pd.DataFrame, key: str, value: int) -> pd.DataFrame:
        return data[data[key] < value]

    @staticmethod
    def is_above(data: pd.DataFrame, key: str, value: int) -> pd.DataFrame:
        return data[data[key] > value]
