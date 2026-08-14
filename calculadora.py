def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    if cupom == "DEVOPS10":
        desconto_percentual += 10

    total = subtotal - (subtotal * desconto_percentual / 100)

    return round(total, 2)