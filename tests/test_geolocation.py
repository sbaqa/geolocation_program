import pytest
from system.command import CmdExec
from system.command import COMMANDS

@pytest.mark.tc1
def test_available_coordinates():
    data = CmdExec.execute_command(COMMANDS['VALID_CITY'])
    assert "lat" in data[0] and "lon" in data[0], f"lat/lon not found in data[0]: {data[0]}"

@pytest.mark.tc2
def test_valid_city_state():
    data = CmdExec.execute_command(COMMANDS['VALID_CITY_STATE'])
    assert data[0]['name'] == "Madison" and data[0]['state'] == "Wisconsin"
    assert data[1]['name'] == "Wi" and data[1]['state'] == "Northwest"

@pytest.mark.tc3
def test_valid_zip_code():
    data = CmdExec.execute_command(COMMANDS['VALID_ZIP_CODE'])
    assert data[0]["zip"] == "10001" and data[0]['name'] == "New York"

@pytest.mark.tc4
def test_multiple_locations():
    data = CmdExec.execute_command(COMMANDS['VALID_MULTIPLE_LOCATIONS'])
    assert data[1]['country'] == "CM" and data[1]['name'] == "Wi"
    assert data[2]['country'] == "US" and data[2]['name'] == "Schenectady"

@pytest.mark.tc5
def test_invalid_location():
    data = CmdExec.execute_command(COMMANDS['INVALID_LOCATION'])
    assert data[0] == {}  # Expect empty response for first invalid location and returned random location in second dict
    assert "lat" in data[1] and "lon" in data[1]
