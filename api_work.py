import requests
import json

pulls_response = requests.get('https://api.github.com/repos/BarabanovaIrina/MentalArithmeticTask/pulls')
pulls_list = json.loads(pulls_response.text)
pulled_branches = [pull['head']['ref'] for pull in pulls_list]

result = json.dumps({"branch": pulled_branches}, indent=4)

with open('api_result.json', 'w', encoding='utf-8') as file:
    file.write(result)
