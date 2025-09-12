from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Now kanzal is here!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)