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

    @staticmethod
    def boolean_stats(data: pd.DataFrame, key: str) -> dict[str, float]:
        true_count = data[key].sum()
        false_count = len(data) - true_count
        return dict(
            true_percentage=(true_count / len(data)) * 100,
            false_percentage=(false_count / len(data)) * 100,
        )

    @staticmethod
    def list_stats(data: pd.DataFrame, key: str) -> dict[str, float]:
        list_lengths = data[key].apply(len)
        return {'min_length': list_lengths.min(), 'max_length': list_lengths.max(),
                'average_length': list_lengths.mean()}
