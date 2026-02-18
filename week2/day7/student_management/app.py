from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_connection, init_db

app = Flask(__name__)
app.secret_key = "supersecretkey"

#INITIALISE DB-----------------
init_db()

#------------------HOME-------------------
@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/students")
    return redirect("/login")

#---------------REGISTER--------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users(username, password) VALUES (%s, %s)",(username, password))
            conn.commit()
        except:
            conn.close()
            return "Username already exists!"
        
        conn.close()
        return redirect("/login")
    
    return render_template("register.html")

#---------------------LOGIN---------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))

        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            return redirect("/students")
        else:
            return "Invalid credential"
        
    return render_template("login.html")

#-----------LOGOUT-------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

#------------STUDENTS--------------
@app.route("/students", methods=["GET", "POST"])
def students():
    if "user_id" not in session:
        return redirect("/login")
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
        conn.commit()
        return redirect("/students")

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("students.html", students=data)

#---------------DELETE----------------
@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        return redirect("/login")
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/students")

if __name__ == "__main__":
    app.run(debug=True)