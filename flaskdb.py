from flask import Flask, render_template
import csv
import json
from pymongo import MongoClient
from flask_cors import CORS
from flask_pymongo import PyMongo

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

def read_data():
    with open("config.json", "r") as config_file:
        config = json.laod(config_file)
    return config

config = read_data()
client = MongoClient(config["connection"])
db = client[config["db_name"]]
images = db[config["images_collection"]]
articles = db[config["articles_collection"]]

print("connected")

app = Flask(__name__)
#send a request to server
cors = CORS(app)


@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/phw')
def phw():
    return render_template('phw.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

if __name__ == "__main__":
    app.run(debug = True)
