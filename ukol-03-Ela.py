import json

with open ('body.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

prospech = {}
for jmeno, body in data.items():
    if body >= 60:
        prospech[jmeno] = "Pass"
    else:
        prospech[jmeno] = "Fail"

print(prospech)

with open("prospech.json", mode="w", encoding="utf-8") as file2:
    json.dump(prospech, file2, ensure_ascii=False, indent=4)