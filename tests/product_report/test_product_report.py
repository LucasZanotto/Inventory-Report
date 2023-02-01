from inventory_report.inventory.product import Product


def test_relatorio_produto():
    objeto2 = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "1LAJK32",
        "ao abrigo de luz",
    )
    frase1 = (
        f"O produto {objeto2.nome_do_produto}"
        f" fabricado em {objeto2.data_de_fabricacao}"
        f" por {objeto2.nome_da_empresa} com validade"
        f" até {objeto2.data_de_validade} "
        f"precisa ser armazenado {objeto2.instrucoes_de_armazenamento}."
    )
    assert str(objeto2) == frase1
