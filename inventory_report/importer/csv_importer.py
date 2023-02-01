import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        file1 = path
        if file1[-4:] != ".csv":
            raise ValueError("Arquivo inválido")
        with open(path) as import_file:
            company_list = csv.DictReader(import_file)
            company_list1 = []
            for companies in company_list:
                company_list1.append(companies)
            return company_list1
