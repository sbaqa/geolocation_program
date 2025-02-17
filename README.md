# Geolocation Utility

This is a command-line utility to fetch geolocation data (latitude, longitude, and place details) from OpenWeather Geocoding API based on city/state or ZIP code input. Fully specified task for this program development you can find here using a [link](https://fetch-hiring.s3.amazonaws.com/SDET/Fetch_Coding_Exercise_SDET_v2.pdf)

## Prerequisites
- Python 3.7+
- `pip` package manager

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the command with the `--locations` flag followed by city/state or ZIP codes:
```sh
python geolocation_utility.py --locations Madison, WI 10001
```
Example output:
```json
{"name": "Madison", "lat": 43.0731, "lon": -89.4012, "state": "Wisconsin"}
{"zip": "10001", "lat": 40.7128, "lon": -74.0060, "city": "New York"}
```

## Running Tests
1. **Ensure dependencies are installed** (see Installation section).
2. **Run tests from the core project folder using pytest:**
   ```sh
   pytest
   ```

## Notes
- This utility only supports locations within the United States.
- It uses the OpenWeather Geocoding API.

## License
This project is open-source and available under the MIT License.

