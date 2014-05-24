#!/user/bin/python
from flask import Flask
from flask import jsonify

app = Flask(__name__)

strength = -100

@app.route("/")
def welcome():
    return "welcome to blueberry"


@app.route("/strength")
def strength():
    f = open('./bluetooth.status', 'r')
    strength = int(f.readlines()[0])
    return jsonify(strength=strength)
    f.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
