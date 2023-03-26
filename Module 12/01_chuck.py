import requests
import json

# https://api.tvmaze.com/search/shows?q= on JSON jonka palveluntarjoaja päättää itse
response = requests.get('https://api.chuchnorris.io/jokes/random')
data = json.loads(response.text)
joke = data['Value']

print(joke)


