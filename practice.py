import requests

api_key = '93715fd4-2fef-4a4b-a502-de4e7a64276e'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)