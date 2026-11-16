import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response into a Python dictionary
    print(data)
    print("Title:", data["title"])
else:
    print(f"Error: {response.status_code}")