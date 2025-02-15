import os
from typing import Optional

import pandas as pd
import yaml


class DataManager:
    def get_data(self, file_path: str, file_type: str) -> pd.DataFrame:
        match file_type:
            case "csv":
                data = pd.read_csv(file_path)
            case "json":
                data = pd.read_json(file_path)
            case "yaml":
                data = self.get_yaml_data(file_path)
            case "xml":
                data = pd.read_xml(file_path)
            case _:
                raise ValueError(f"Unsupported file type: {file_type}")
        if "grades" in data.columns:
            data["grades"] = (
                data["grades"]
                .apply(lambda x: x.split(","))
                .apply(lambda x: [int(i.replace("[", "").replace("]", "")) for i in x])
            )
        return data

    @staticmethod
    def get_yaml_data(file_path: str) -> pd.DataFrame:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return pd.DataFrame(data)

    @staticmethod
    def save_data(data: pd.DataFrame, file_name: str, file_format: str):
        match file_format:
            case "csv":
                data.to_csv(file_name, index=False)
            case "json":
                data.to_json(file_name, orient="records")
            case "xml":
                if "grades" in data.columns:
                    data["grades"] = data["grades"].apply(str)
                data.to_xml(file_name)
            case "yaml":
                data_dict = data.to_dict(orient="records")
                with open(file_name, "w") as file:
                    yaml.dump(data_dict, file)
            case _:
                raise ValueError(f"Unsupported file format: {file_format}")
