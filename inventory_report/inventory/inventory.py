import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_csv(path):
        with open(path) as import_file:
            company_list = csv.DictReader(import_file)
            company_list1 = []
            for companies in company_list:
                company_list1.append(companies)
            return company_list1

    def read_json(path):
        with open(path) as import_file:
            company_list = json.load(import_file)
            company_list1 = []
            for companies in company_list:
                company_list1.append(companies)
            return company_list1

    def read_xml(path):
        with open(path) as import_file:
            company_list = xmltodict.parse(import_file.read())
            # print(company_list["dataset"]["record"])
            return company_list["dataset"]["record"]

    def read_path(path):
        file1 = path
        if file1[-4:] == ".csv":
            return Inventory.read_csv(path)
        elif file1[-5:] == ".json":
            return Inventory.read_json(path)
        elif file1[-4:] == ".xml":
            return Inventory.read_xml(path)

    @staticmethod
    def import_data(path, type):
        company_list1 = Inventory.read_path(path)
        if type == "simples":
            return SimpleReport.generate(company_list1)
        elif type == "completo":
            return CompleteReport.generate(company_list1)
