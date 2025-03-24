import requests


def get_city_by_coordinates(lat: float, lon: float) -> str:
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=10&addressdetails=1"
    headers = {"User-Agent": "TelegramBot"}

    response = requests.get(url, headers=headers)
    data = response.json()

    if "address" in data and "city" in data["address"]:
        return data["address"]["city"]
    elif "address" in data and "town" in data["address"]:
        return data["address"]["town"]
    elif "address" in data and "village" in data["address"]:
        return data["address"]["village"]
    else:
        return "Город не найден"
