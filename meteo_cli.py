"""
Outil en ligne de commande pour avoir la météo dans sa ville
utilisant l'api:

A revoir à l'occasion:
    - nommage des fonctions
    - gestion des execeptions
    - Sortie plus détaillée et à verifier
"""

import requests


def localisation_url(city: str) -> str:
    return f"https://geocoding-api.open-meteo.com/v1/search?name={ city }&count=10&language=fr&format=json"


def meteo_url(request: dict) -> str:
    return f"https://api.open-meteo.com/v1/forecast?latitude={ request["latitude"] }&longitude={ request["longitude"] }&hourly=temperature_2m&models=meteofrance_seamless&forecast_days=4"


def read_user_city() -> str:
    print("Entrez votre ville:")
    city = input().strip()
    return city


def get_city_weather(city: str) -> str:
    localisation_url_call = localisation_url(city)
    response = requests.get(localisation_url_call)
    data = response.json()

    meteo_france_request = {"latitude": 0.0, "longitude": 0.0}
    meteo_france_request["latitude"] = data["results"][0]["latitude"]
    meteo_france_request["longitude"] = data["results"][0]["longitude"]

    meteo_url_call = meteo_url(meteo_france_request)
    meteo_response = requests.get(meteo_url_call)
    data = meteo_response.json()

    return str(data["hourly"]["temperature_2m"][-1])


def main():
    user_input = read_user_city()
    weather = get_city_weather(user_input)
    print(weather)


if __name__ == "__main__":
    main()
