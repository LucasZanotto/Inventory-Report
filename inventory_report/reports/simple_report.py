from datetime import datetime
import collections


class SimpleReport:
    @staticmethod
    def generate(list):
        list_list = list
        fabricacao_list = []
        validation_list = []
        empresa_list = []
        variavel_de_hoje = datetime.today().strftime("%Y-%m-%d")
        for dicionario in list_list:
            fabricacao_list.append(dicionario["data_de_fabricacao"])

        for dicionario in list_list:
            if dicionario["data_de_validade"] >= str(variavel_de_hoje):
                validation_list.append(dicionario["data_de_validade"])

        data_de_fabricacao_antiga = min(fabricacao_list)
        data_de_fabricacao_nova = min(validation_list)

        for empresa in list:
            empresa_list.append(empresa["nome_da_empresa"])

        empresa_max = collections.Counter(empresa_list)
        return f"""Data de fabricação mais antiga: {data_de_fabricacao_antiga}
Data de validade mais próxima: {data_de_fabricacao_nova}
Empresa com mais produtos: {empresa_max.most_common(1)[0][0]}"""


# empresa1 = SimpleReport.generate(
#     [
#         {
#             "id": 1,
#             "nome_do_produto": "CADEIRA",
#             "nome_da_empresa": "Forces of Nature",
#             "data_de_fabricacao": "2022-04-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "Conservar em local fresco",
#         }
#     ]
# )

# print(empresa1)

# dia = datetime.today().strftime("%Y-%m-%d")
# print(dia)
