import pandas as pd
import yaml


class DataManager:
    def get_data(self, file_path: str, file_type: str) -> pd.DataFrame:
        match file_type:
            case "csv":
                return pd.read_csv(file_path)
            case "json":
                return pd.read_json(file_path)
            case "yaml":
                return self.get_yaml_data(file_path)
            case "xml":
                return pd.read_xml(file_path)
            case _:
                raise ValueError(f"Unsupported file type: {file_type}")

    @staticmethod
    def get_yaml_data(file_path: str) -> pd.DataFrame:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return pd.DataFrame(data)
