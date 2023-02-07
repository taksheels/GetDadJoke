import requests

def get_dad_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if response.status_code == 200:
        return response.json()["joke"]
    else:
        return "Failed to fetch a dad joke. Please try again later."

joke = get_dad_joke()
print(joke)
