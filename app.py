from flask import Flask
from types.models.Customer import Customer

app = Flask(__name__)


@app.route("/")
def hello_world():
    t = Customer("qwert")
    return "<p>Hello, World!</p>"
