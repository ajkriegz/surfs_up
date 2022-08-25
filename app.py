from flask import Flask
app = Flask(__name__)
@app.route('/') # Define the root, the starting point
def hello_world():
    return 'Hello world'