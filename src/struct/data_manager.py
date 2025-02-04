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
