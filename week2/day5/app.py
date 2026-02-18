from flask import Flask, render_template, request, redirect,url_for
import mysql.connector

app = Flask(__name__)

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password",
            database="student_detail"
        )
        return conn
    except mysql.connector.Error as err:
        print("Database Connection Error: ", err)
        return None
    
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        course = request.form.get("course")

        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO students (name, age, course) VALUES(%s, %s, %s)"
        values = (name, age, course)
        cursor.execute(query, values)

        conn.commit()
        cursor.close()
        conn.close()

    return render_template("home.html")

@app.route("/students")
def students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("students.html", students=data)

@app.route("/delete/<int:id>")
def delete_function(id):
    conn = get_connection
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("students"))




if __name__ == "__main__":
    app.run(debug=True)