import pandas as pd


class FilterManager:
    @staticmethod
    def filter_string(data: pd.DataFrame, key: str, filter_value: str) -> pd.DataFrame:
        """
        Filtre les données en fonction d'une chaîne de caractères.
        """
        if key in data.columns:
            return data[
                data[key].astype(str).str.contains(filter_value, case=False, na=False)
            ]
        return data

    @staticmethod
    def filter_numeric(
        data: pd.DataFrame, key: str, filter_value: float, operation: str
    ) -> pd.DataFrame:
        """
        Filtre les données en fonction d'une valeur numérique et d'une opération (>, <, =).
        """
        if key in data.columns:
            if operation == ">":
                return data[data[key] > filter_value]
            elif operation == "<":
                return data[data[key] < filter_value]
            elif operation == "=":
                return data[data[key] == filter_value]
        return data

    @staticmethod
    def filter_boolean(
        data: pd.DataFrame, key: str, filter_value: bool
    ) -> pd.DataFrame:
        """
        Filtre les données en fonction d'une valeur booléenne.
        """
        if key in data.columns:
            return data[data[key] == filter_value]
        return data
