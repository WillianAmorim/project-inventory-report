from typing import Dict, List, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product

import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        list_products = []

        with open(self.path) as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item['id'],
                item['product_name'],
                item['company_name'],
                item['manufacturing_date'],
                item['expiration_date'],
                item['serial_number'],
                item['storage_instructions'],
            )

            list_products.append(product)

        return list_products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
