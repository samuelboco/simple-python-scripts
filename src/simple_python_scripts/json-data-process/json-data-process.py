import requests
import os

url = input("Enter API URL: ")
key = input("Enter Dictionary Key: ")

# TEST URL : "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.get(url)
except Exception as e:
    print(f"Unable get API data: {e}")
    os._exit(1)


def contains_key(value, key):
    if isinstance(value, dict):
        return key in value or any(
            contains_key(item, key) for item in value.values()
        )
    return False

data = response.json()  

if response.status_code != 200:
    print(f"Unable get API data: Response {response.status_code}") 

if contains_key(data, key):
    print(f"{key}:", data[key])
else:
    print(f"Unable to find key: {key}") 