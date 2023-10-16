import json

with open ('body.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

for jmeno, body in data.items():
    if body >= 60:
        print(jmeno,":", "Pass")
    else:
         print(jmeno,":", "Fail")