import requests, html

parameters = {
    "amount" : 10,
    "type" : "boolean"
}

r = requests.get("https://opentdb.com/api.php", params=parameters)
r.raise_for_status()
data = r.json()
question_api_data = data["results"]

for item in question_api_data:
    item["question"] = html.unescape(item["question"])    
