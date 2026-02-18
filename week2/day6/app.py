from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecretkey"

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password",
            database="ai_grind"
        )
        return conn
    except mysql.connector.Error as err:
        print("Database Connection Error: ", err)
        return None

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()

        except:
            return "Username already exists!"
        
        cursor.close()
        conn.close()
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            return redirect(url_for("students"))
        else:
            return "Invalid credetial"
        
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

#======Protected STUDENTS ROUTE==========
@app.route("/students", methods=["GET", "POST"])
def students():
    #Login Protection
    if "user" not in session:
        return redirect(url_for("login"))
    conn = get_connection()
    cursor = conn.cursor()
    
    

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        course = request.form.get("course")

        

        cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
        conn.commit()
        return redirect(url_for("students"))
    
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("students.html", students= data)

if __name__ == "__main__":
    app.run(debug=True)
    


    
