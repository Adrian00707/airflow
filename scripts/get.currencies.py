import requests


def fetch_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    print(data)


if __name__ == "__main__":
    fetch_currencies()
