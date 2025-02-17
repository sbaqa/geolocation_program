import argparse
from openweather_api.geoprocessor import GeoProcessor

def activate_parsing():
    parser = argparse.ArgumentParser(description="Get geolocation data for given locations.")
    parser.add_argument("--locations", nargs='+', required=True, help="List of locations (city, state or zip code)")
    args = parser.parse_args()
    return args

def main():
    """ Add argument to the CLI that will process the specified data through CLI command """
    args = activate_parsing()
    locations_data = GeoProcessor.process_locations(args.locations)

    for i in locations_data:
        print(i)

if __name__ == "__main__":
    main()
