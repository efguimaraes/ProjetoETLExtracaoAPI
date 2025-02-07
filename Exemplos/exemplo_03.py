import requests

url = 'https://api.coinbase.com/v2/prices/spot'
header = {
        "Accept": "application/json",
        "User-Agent":"MinhaAplicacao/1.0"
}
params = {"currency": "USD"} #Moeda da Consulta

response = requests.get(url, headers=header, params=params)

data = response.json()

print("Preço do Bitcoin (USD):", data["data"]["amount"])