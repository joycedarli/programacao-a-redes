import httpx

def obter_cotacao_dolar(data):
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json"

    try:
        response = httpx.get(url)
        data = response.json()

        if 'value' in data and len(data['value']) > 0:
            cotacao = data['value'][0]['cotacaoCompra']
            return cotacao

    except httpx.RequestError as e:
        print(f"Erro na requisição: {e}")

    return None

data = input("Digite a data (dd/mm/aaaa): ")

# Formato da data esperado pela API: MM-DD-AAAA
data_formatada = data[3:5] + '-' + data[0:2] + '-' + data[6:10]

cotacao = obter_cotacao_dolar(data_formatada)

if cotacao:
    print(f"A cotação do dólar em {data} é {cotacao}")
else:
    print("Não foi possível obter a cotação do dólar para a data especificada.")