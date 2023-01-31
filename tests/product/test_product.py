from inventory_report.inventory.product import Product

# frase = "O produto secador fabricado em 2020-10-10 por seca_Limpo com
# validade até 2030-10-11 precisa ser armazenado guardar na caixa."


def test_cria_produto():
    objeto1 = Product(
        1,
        "secador",
        "seca_Limpo",
        "2020-10-10",
        "2030-10-11",
        "1LAJK32",
        "guardar na caixa",
    )

    assert objeto1.id == 1
    assert objeto1.nome_do_produto == "secador"
    assert objeto1.nome_da_empresa == "seca_Limpo"
    assert objeto1.data_de_fabricacao == "2020-10-10"
    assert objeto1.data_de_validade == "2030-10-11"
    assert objeto1.numero_de_serie == "1LAJK32"
    assert objeto1.instrucoes_de_armazenamento == "guardar na caixa"
