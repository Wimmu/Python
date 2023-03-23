import requests
import json

hakusana = input("Anna hakusana:")

# https://api.tvmaze.com/search/shows?q= on JSON jonka palveluntarjoaja päättää itse
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:
    vastaus = requests.get(pyynto) #.json()
    #print(json.dumps(vastaus, indent=1))
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa!")

