from flask import Flask

app = Flask(__name__)

@app.route('/images')
def images():
    return 'images'