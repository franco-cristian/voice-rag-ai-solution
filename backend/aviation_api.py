import requests
import os

def get_flight_info(origin_city, destination_city):
    """Consultar información de vuelos usando la API de AviationStack."""
    api_key = os.getenv("AVIATIONSTACK_API_KEY")
    endpoint = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": api_key,
        "dep_iata": origin_city,
        "arr_iata": destination_city
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        flights = response.json().get("data", [])
        if flights:
            return f"Se encontraron vuelos de {origin_city} a {destination_city}."
        else:
            return "No se encontraron vuelos."
    return "Error consultando la API de vuelos."
