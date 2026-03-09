import requests
import json

# 1. Define the API endpoint
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    # 2. Send the GET request
    response = requests.get(url)

    # 3. Check if the request was successful (Status Code 200)
    if response.status_code == 200:
        
        # 4. Parse the JSON data
        # Option A: Using the built-in requests method
        user_data = response.json()
        
        # Option B: Using the json library explicitly
        # user_data = json.loads(response.text)

        # 5. Access specific data
        name = user_data.get("name")
        email = user_data.get("email")
        city = user_data.get("address", {}).get("city")

        print(f"--- User Profile ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Location: {city}")
        
        # 6. Pretty-print the entire JSON object
        print("\n--- Full Raw Data ---")
        print(json.dumps(user_data, indent=4))

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")