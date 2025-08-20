# Custom Exceptions
class InvalidDeviceTypeException(Exception):
    pass

class WeakWiFiConnectionException(Exception):
    pass

class InvalidInstallationLocationException(Exception):
    pass

class InvalidFirmwareVersionException(Exception):
    pass


def validate_device(device_type, wifi_signal_strength, location, firmware_version):
    valid_devices = ["Smart Light", "Smart Thermostat", "Smart Lock"]
    valid_locations = ["Living Room", "Bedroom", "Kitchen"]

    if device_type not in valid_devices:
        raise InvalidDeviceTypeException("Invalid device type.")

    if wifi_signal_strength < 3:
        raise WeakWiFiConnectionException("Weak Wi-Fi connection.")

    if location not in valid_locations:
        raise InvalidInstallationLocationException("Invalid installation location.")

    if firmware_version < 2.0:
        raise InvalidFirmwareVersionException("Invalid firmware version.")

    # If all validations pass
    signal_quality_index = (wifi_signal_strength * firmware_version) / 2
    return signal_quality_index


# Main program
try:
    # Sample inputs
    device_type = input("Enter device type: ")
    wifi_signal_strength = int(input("Enter Wi-Fi signal strength (bars): "))
    location = input("Enter installation location: ")
    firmware_version = float(input("Enter firmware version: "))

    result = validate_device(device_type, wifi_signal_strength, location, firmware_version)
    print(f"Signal Quality Index: {result:.2f}")

except (InvalidDeviceTypeException,
        WeakWiFiConnectionException,
        InvalidInstallationLocationException,
        InvalidFirmwareVersionException) as e:
    print("Error:", e)
except ValueError:
    print("Error: Invalid input type.")