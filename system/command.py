import subprocess
import ast

COMMANDS = {
    "VALID_CITY": "python geolocation_utility.py --locations Madison",
    "VALID_CITY_STATE": "python geolocation_utility.py --locations Madison, WI",
    "VALID_ZIP_CODE": "python geolocation_utility.py --locations 10001",
    "VALID_MULTIPLE_LOCATIONS": "python geolocation_utility.py --locations Madison, WI 12345",
    "INVALID_LOCATION": "python geolocation_utility.py --locations InvalidCity, ZZ"
}

class CmdExec:
    def execute_command(command):
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        list_of_strings = cmd.communicate()[0].strip().split('\n')

        country_list = []
        for item in list_of_strings:
            item = item.strip()  # Remove any unnecessary whitespace around the string
            if item:
                try:
                    # Try to evaluate the string into a dictionary
                    country_list.append(ast.literal_eval(item))
                except (SyntaxError, ValueError, IndexError) as e:
                    print(f"Skipping invalid string: {item}, Error: {e}")

        return country_list
