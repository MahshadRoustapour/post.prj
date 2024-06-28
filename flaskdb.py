from flask import Flask, render_template, jsonify
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

def read_json(jsonname):
    with open(jsonname, "r", encoding = 'utf-8') as jsonfile:
        data = json.laod(jsonfile)
    return data
    
csvfile = 'images.csv'
json_file = 'images.json'
csv_to_json(csvfile, json_file)

csvfile2 = 'articles.csv'
jsonfile2 = 'articles.json'
csv_to_json(csvfile2, jsonfile2)

images_data = read_json(json_file)
articles_data = read_json(json_file)

client = MongoClient("mongodb://localhost:27017")
db = client["post.prj"]
images_collection = db["images"]
articles_collection = db["articles"]

images_collection.delete_many({})
images_collection.insert_many(images_data)

articles_collection.delete_many({})
articles_collection.insert_many(articles_data)

print("data inserted into mongoDB")

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
