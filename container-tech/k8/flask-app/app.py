from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        with open("/flask/env/test.txt", "r") as f:
            line = f.readline()
            return line + "\n"
    except Exception as e:
        return "Exception:{0}".format(e)