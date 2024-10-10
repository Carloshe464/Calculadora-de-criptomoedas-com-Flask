from cotacao_spot import obter_cotacao_spot


def compra(valor_moeda_em_dolar, total_de_moedas, api_key, base_currency, target_currency):
    preco = valor_moeda_em_dolar
    posicao = total_de_moedas

    try:
        posicao = float(posicao)
        preco = float(preco)
    finally:

        posicao_dolar = posicao * preco

    api_key = 'fc8936dc03264db5b0c9440586d6c5ee'
    base_currency = 'USD'
    target_currency = 'BRL'

    cotacao = obter_cotacao_spot(api_key, base_currency, target_currency)

    
    if cotacao is not None:
        total_carteira = posicao_dolar * cotacao
        return total_carteira
    else:
        print(f'Não foi possivel obter a cotacao.')
        return None



