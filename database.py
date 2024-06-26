import csv
import json

def csv_to_json(csvname, jsonname):

    filec = open(csvname)
    data = csv.DictReader(filec)
    data_dict = []
 
    for rows in data:
        data_dict.append(rows)

    with open(jsonname, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data_dict, indent = 4))
    
csvfile = 'images.csv'
json_file = 'images.json'
csv_to_json(csvfile, json_file)

csvfile2 = 'articles.csv'
jsonfile2 = 'articles.json'
csv_to_json(csvfile2, jsonfile2)

