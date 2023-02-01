import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        file1 = path
        if file1[-4:] != ".xml":
            raise ValueError("Arquivo inválido")
        with open(path) as import_file:
            company_list = xmltodict.parse(import_file.read())
            return company_list["dataset"]["record"]
