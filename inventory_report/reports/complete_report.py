from inventory_report.reports.simple_report import SimpleReport
import collections


class CompleteReport(SimpleReport):
    def generate(list):
        relatorio_simples = SimpleReport.generate(list)
        list_relatos = list
        empresa_list = []
        for dicionario in list_relatos:
            empresa_list.append(dicionario["nome_da_empresa"])
        # print(empresa_list)
        ranking_de_empresas = collections.Counter(empresa_list)
        # print(ranking_de_empresas)
        leaderboard = ""
        for rank in ranking_de_empresas:
            # print(rank)
            # print(ranking_de_empresas[rank])
            leaderboard += f"\n- {rank}: {ranking_de_empresas[rank]}"
        return (
            relatorio_simples
            + "\n"
            + "Produtos estocados por empresa:"
            + leaderboard
            + "\n"
        )


if __name__ == "__main__":
    empresa2 = CompleteReport.generate(
        [
            {
                "id": 1,
                "nome_do_produto": "CADEIRA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-04-04",
                "data_de_validade": "2023-02-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar em local fresco",
            },
            {
                "id": "2",
                "nome_do_produto": "fentanyl citrate",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2020-12-06",
                "data_de_validade": "2023-12-25",
                "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
                "instrucoes_de_armazenamento": "instrucao 2",
            },
            {
                "id": "3",
                "nome_do_produto": "NITROUS OXIDE",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2020-12-22",
                "data_de_validade": "2024-11-07",
                "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
                "instrucoes_de_armazenamento": "instrucao 3",
            },
            {
                "id": "4",
                "nome_do_produto": "Norepinephrine Bitartrate",
                "nome_da_empresa": "Cantrell Drug Company",
                "data_de_fabricacao": "2020-12-24",
                "data_de_validade": "2025-08-19",
                "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
                "instrucoes_de_armazenamento": "instrucao 4",
            },
            {
                "id": "5",
                "nome_do_produto": "Norepinephrine Bitartrate",
                "nome_da_empresa": "Cantrell Drug Company",
                "data_de_fabricacao": "2020-12-24",
                "data_de_validade": "2025-08-19",
                "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
                "instrucoes_de_armazenamento": "instrucao 4",
            },
            {
                "id": "6",
                "nome_do_produto": "Norepinephrine Bitartrate",
                "nome_da_empresa": "Norton",
                "data_de_fabricacao": "2020-12-24",
                "data_de_validade": "2025-08-19",
                "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
                "instrucoes_de_armazenamento": "instrucao 4",
            },
        ]
    )

    print(empresa2)
    print("oi")

print("oi2")
