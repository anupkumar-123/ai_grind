from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running"

@app.route("/about")
def menu():
    return "Hello, Flask is about to launch"

if __name__ == "__main__":
    app.run(debug=True)
