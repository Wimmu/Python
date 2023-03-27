import requests
import json

pyyntö = "https://api.chuchnorris.io/jokes/random?"

vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()

print(json_vastaus["value"])


