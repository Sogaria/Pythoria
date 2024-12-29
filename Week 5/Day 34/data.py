import requests

r = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_api_data = r.json()

for item in question_api_data["results"]:
    print(item["question"])
    print(item["correct_answer"])


