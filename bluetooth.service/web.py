#!/user/bin/python
from flask import Flask
from flask import jsonify

app = Flask(__name__)

strength = -100

@app.route("/")
def welcome():
    return jsonify(welcome="welcome to blueberry")

@app.route("/strength")
def strength():
    f = open('./bluetooth.status', 'r')
    lines = f.readlines()
    if len(lines) > 0:
        strength = int(lines[0])
    else:
        print 'someone fucked up'
        strength = -1000000
    return jsonify(strength=strength)
    f.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True)
