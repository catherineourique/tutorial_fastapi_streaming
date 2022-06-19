import requests

response = requests.get('http://localhost:7779/test', stream=True)

for r in response.iter_lines():
    print(r)
    print('passei uma linha')
