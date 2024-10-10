import requests


def obter_cotacao_spot(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    params = {'apikey': api_key}

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        resposta_json = response.json()
        rates = resposta_json.get('rates', {})
        spot_rate = rates.get(target_currency)
        return spot_rate
    else:
        print(f"Erro ao realizar a consulta da cotação: {response.status_code}")
        return None
    

api_key = 'fc8936dc03264db5b0c9440586d6c5ee'
base_currency = 'USD'
target_currency = 'BRL'

cotacao_spot = obter_cotacao_spot(api_key, base_currency, target_currency)


#if cotacao_spot is not None:
#   print(f'Cotacao spot de {base_currency} para {target_currency}:{cotacao_spot} ')
#else:
#    print(f'Não foi possivel obter a cotacao atual.')
