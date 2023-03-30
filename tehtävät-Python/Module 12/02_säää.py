import requests
import json

# Kysy käyttäjältä paikkakunta
city = input("Syötä paikkakunta: ")

# API-pyynnön osoite
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=895f29bb7f89a74190b92992ef6a6c59"

# Lähetä API-pyyntö
response = requests.get(url)

# Tarkista, onko vastaus onnistunut
if response.status_code == 200:
    # Muunna vastaus JSON-muotoon
    data = json.loads(response.text)
    # Hae lämpötila ja muunna Celsius-asteiksi
    temperature = round(data['main']['temp'] - 273.15, 1)
    # Hae säätilan kuvaus
    description = data['weather'][0]['description'].capitalize()
    # Tulosta säätila
    print(f"Säätila paikkakunnalla {city}: {description}, {temperature} °C")
else:
    # Tulosta virheilmoitus
    print("Säätilaa ei löytynyt.")