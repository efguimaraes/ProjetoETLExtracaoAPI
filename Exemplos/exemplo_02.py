import requests

url = 'https://jsonplaceholder.typicode.com/comments'
params = {"postId":1} #obter apenas comentaorios do post 1
response = requests.get(url, params=params)

comentarios = response.json()

print(f"foram encontrados {len(comentarios)} comentarios.")
print(f"Erro: {response.status_code} - {response.text}")