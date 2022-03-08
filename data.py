import requests


peramiters = {
    "amount": 10,
    "type": "boolean"
}

request = requests.get("https://opentdb.com/api.php", params=peramiters)
request.raise_for_status()
data = request.json()


question_data = data["results"]
