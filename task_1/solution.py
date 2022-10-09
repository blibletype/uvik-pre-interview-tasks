import csv
import json

dict = {}
countries = []

with open('task_1/data.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        countries.append(row['country'])

    countries = list(dict.fromkeys(countries))
        
for country in countries:
    dict[country] = {
            'peoples': [],
            'count': 0
        }
    peoples = []
    with open('task_1/data.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == country:
                peoples.append(row[1])
        dict[country]['peoples'] = peoples
        dict[country]['count'] = len(peoples)

print(json.dumps(dict, indent=4))