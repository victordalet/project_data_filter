import pandas as pd


class FilterManager:
    @staticmethod
    def contains(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key].str.contains(value, na=False)]

    @staticmethod
    def equals(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key] == value]

    @staticmethod
    def start_with(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key].str.startswith(value)]

    @staticmethod
    def finish_with(data: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
        return data[data[key].str.endswith(value)]
