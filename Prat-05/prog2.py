# Usar numpy e requests. Consultar api, extrair informacao e calcular a soma dos id

import requests
import numpy as np

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

dados = response.json()

ids = []

for item in dados:
    ids.append(item[ids])

ids_list = np.array(ids)

print(f"A soma dos ids: {np.sum(ids_list)}")