import requests
api_url = "https://jsonplaceholder.typicode.com/posts"

result = requests.get(url)

print(f"Dados do API: {result}")
