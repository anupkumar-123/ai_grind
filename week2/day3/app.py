from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        return render_template("result.html", name=name, age=age)
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)