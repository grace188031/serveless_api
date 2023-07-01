import json

with open('result.json','r') as file:
    json_pretty = file.read()

    json_pretty = json.loads(json_pretty)

json_pretty = json.dumps(json_pretty, indent=4)

with open('jsone_pretty','w') as file:
    file.write(json_pretty)
