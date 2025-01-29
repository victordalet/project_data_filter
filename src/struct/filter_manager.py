import pandas as pd


class FilterManager:
    @staticmethod
    def filter_string(data: pd.DataFrame, key: str, filter: str) -> pd.DataFrame:
        return data[data[key] in filter]
