import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

type_data= data["current"]

type_data




def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")


def fetch_users():
    url="https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        print(f"Successfully fetched{len(users)} users:\n")
        for user in users:
            print(f"Name: {user['name']} | Email: {user['email']} ")

    else:
        print(f"Failed to retrive data. Status Code: {response.status_code}")

fetch_users()




# How it works
# You send a request to the API’s URL with parameters (like coordinates)
# The API processes your request and finds the data
# You receive JSON data back with the information
# You extract the specific parts you need



import requests

def get_current_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Define the parameters as a dictionary
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    
    # requests automatically encodes the dictionary into the URL string
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['current_weather']['temperature']
        print(f"Current temperature at coordinates ({lat}, {lon}): {temp}°C")
    else:
        print("Failed to fetch weather data.")

# Coordinates for London
get_current_temperature(51.5074, -0.1278)



import requests

def create_new_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # The data we want to send to the API
    new_post_data = {
        "title": "Learning Python APIs",
        "body": "This is a test post to demonstrate POST requests.",
        "userId": 1
    }
    
    # Use the 'json' parameter to automatically set the Content-Type header 
    # to application/json and serialize the dictionary
    response = requests.post(url, json=new_post_data)
    
    # 201 is the standard HTTP status code for "Created"
    if response.status_code == 201:
        created_post = response.json()
        print("Post created successfully!")
        print(f"Server returned ID: {created_post['id']}")
        print(f"Title: {created_post['title']}")
    else:
        print(f"Failed to create post. Status: {response.status_code}")

create_new_post()

import requests

def fetch_secure_data():
    url = "https://httpbin.org/bearer"
    
    # Define headers, including the Authorization Bearer token
    headers = {
        "Authorization": "Bearer my_super_secret_token_123",
        "User-Agent": "MyPythonApp/1.0"
    }
    
    try:
        # A timeout prevents the script from hanging indefinitely if the server is down
        response = requests.get(url, headers=headers, timeout=5)
        
        # This will automatically raise an exception for 4xx or 5xx status codes
        response.raise_for_status() 
        
        data = response.json()
        print("Authentication successful!")
        print("Token verified by server:", data['token'])
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} (Check your token or URL)")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Check your internet.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

fetch_secure_data()

