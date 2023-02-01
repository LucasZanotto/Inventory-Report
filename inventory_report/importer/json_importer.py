import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        file1 = path
        if file1[-5:] != ".json":
            raise ValueError("Arquivo inválido")
        with open(path) as import_file:
            company_list = json.load(import_file)
            company_list1 = []
            for companies in company_list:
                company_list1.append(companies)
            return company_list1
