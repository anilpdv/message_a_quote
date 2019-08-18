import requests

url = 'http://quotesapi.ml/random'

quote = requests.get(url)
print(quote.status_code)
print(quote.json())
