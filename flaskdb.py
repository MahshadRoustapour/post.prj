from flask import Flask

app = Flask(__name__)

@app.route('/images')
def images():
    return 'images'

@app.route('/home')
def home():
    return 'home'

@app.route('/phw')
def phw():
    return 'phw'
