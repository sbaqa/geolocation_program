from openweather_api.geolocator import OpenWeatherAPI
from typing import List, Dict, Any

class GeoProcessor:
    def process_locations(locations: List[str]) -> List[Dict[str, Any]]:
        """Process list of locations and fetch geolocation data."""
        results = []

        for loc in locations:
            if loc.replace(",", "").replace(" ", "").isdigit():
                result = OpenWeatherAPI.get_location_by_zip_code(loc)
            else:
                result = OpenWeatherAPI.get_location_by_city_name(loc)
            results.append(result)

        return results
