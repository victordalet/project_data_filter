import sys
from typing import List
import random
import csv
import json
import yaml
import xml.etree.cElementTree as ET
import names
from src.struct.structur_def import Student, Item

# Définition des produits, catégories et plages de prix
products = {
    "Laptop": {
        "category": "Computers",
        "price_range": (500, 2000),
    },
    "Smartphone": {
        "category": "Electronics",
        "price_range": (100, 1500),
    },
    "Tablet": {
        "category": "Electronics",
        "price_range": (150, 1200),
    },
    "Headphones": {
        "category": "Accessories",
        "price_range": (20, 500),
    },
    "Smartwatch": {
        "category": "Accessories",
        "price_range": (50, 1000),
    },
    "Camera": {
        "category": "Photography",
        "price_range": (100, 3000),
    },
    "Keyboard": {
        "category": "Accessories",
        "price_range": (10, 200),
    },
    "Mouse": {
        "category": "Accessories",
        "price_range": (5, 150),
    },
    "Monitor": {
        "category": "Computers",
        "price_range": (100, 1000),
    },
    "Charger": {
        "category": "Accessories",
        "price_range": (10, 100),
    },
}

# Liste des produits disponibles
product_names = list(products.keys())


class Main:
    def __init__(self):
        self.extension: str = sys.argv[1]
        self.mode: str = sys.argv[2]
        self.size: int = random.randint(1, 10000)
        self.save_data()

    def create_random_student_data(self) -> List[Student]:
        student_list = []
        for _ in range(self.size):
            student_list.append(
                Student(
                    first_name=names.get_first_name(),
                    last_name=names.get_last_name(),
                    age=random.randint(16, 30),
                    apprentice=True if random.randint(0, 1) == 1 else False,
                    grades=[random.randint(1, 6) for _ in range(5)],
                )
            )
        return student_list

    def create_random_item_data(self) -> List[Item]:
        item_list = []
        for _ in range(self.size):
            product_name = random.choice(product_names)
            product_info = products[product_name]
            item_list.append(
                Item(
                    name=product_name,
                    category=product_info["category"],
                    # Génération du prix dans la plage spécifique au produit et arrondi à 2 décimales
                    price=round(random.uniform(*product_info["price_range"]), 2),
                    quantity=random.randint(1, 100),
                )
            )
        return item_list

    def save_data(self) -> None:
        if self.mode == "student":
            data = self.create_random_student_data()
        else:
            data = self.create_random_item_data()

        match self.extension:
            case "csv":
                self.save_csv(data)
            case "json":
                self.save_json(data)
            case "yaml":
                self.save_yaml(data)
            case "xml":
                self.save_xml(data)
            case _:
                raise ValueError("Invalid extension")

    def save_csv(self, data: List) -> None:
        csv_file = f"data/random_data_{self.mode}.{self.extension}"
        with open(csv_file, mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(data[0].dict().keys())
            for item in data:
                writer.writerow(item.dict().values())

    def save_json(self, data: List) -> None:
        json_file = f"data/random_data_{self.mode}.{self.extension}"
        with open(json_file, mode="w") as file:
            json.dump(data, file, default=lambda x: x.dict())

    def save_yaml(self, data: List) -> None:
        yaml_file = f"data/random_data_{self.mode}.{self.extension}"
        with open(yaml_file, mode="w") as file:
            yaml.dump([item.dict() for item in data], file)

    def save_xml(self, data: List) -> None:
        xml_file = f"data/random_data_{self.mode}.{self.extension}"
        root = ET.Element("root")
        for item in data:
            child = ET.SubElement(root, self.mode)
            for key, value in item.dict().items():
                ET.SubElement(child, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(xml_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tools/create_random_file.py <extension> <mode>")
        sys.exit(1)
    Main()
