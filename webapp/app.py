from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def successfull_connection():
    return "Code 200"

@app.route("/error")
def error_connection():
    abort(500, "Code 500 error!")

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")