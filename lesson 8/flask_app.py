
from flask import Flask


app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello everyone!"


app.run(debug=True, port=5000)
