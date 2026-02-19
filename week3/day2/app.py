from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="ai_grind"
    )

@app.route("/api/students", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Student added sccessfully"})



if __name__ == "__main__":
    app.run(debug=True)









