import pandas as pd


class StatsManager:
    @staticmethod
    def average(data: pd.DataFrame, key: str) -> pd.DataFrame:
        return data[key].mean()

    @staticmethod
    def min(data: pd.DataFrame, key: str) -> pd.DataFrame:
        return data[key].min()

    @staticmethod
    def max(data: pd.DataFrame, key: str) -> pd.DataFrame:
        return data[key].max()
