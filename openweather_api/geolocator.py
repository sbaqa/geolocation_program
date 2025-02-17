import requests
from typing import Dict, Any
from system.config import OPENWEATHER_API_HOSTS

BASE_URL = OPENWEATHER_API_HOSTS["BASE_URL"]
API_KEY = OPENWEATHER_API_HOSTS["API_KEY"]

class OpenWeatherAPI:
    """ Class to interact with OpenWeather Geocoding API """
    
    @staticmethod
    def get_location_by_city_name(city_state: str) -> Dict[str, Any]:
        """Fetch latitude and longitude using city and state."""
        url = f"{BASE_URL}direct?q={city_state}&limit=1&appid={API_KEY}"
        response = requests.get(url)
        return response.json()[0] if response.ok and response.json() else {}

    @staticmethod
    def get_location_by_zip_code(zip_code: str) -> Dict[str, Any]:
        """Fetch latitude and longitude using zip code."""
        url = f"{BASE_URL}zip?zip={zip_code},US&appid={API_KEY}"
        response = requests.get(url)
        return response.json() if response.ok else {}
