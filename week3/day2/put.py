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

@app.route("/api/students/<int:id>", methods=["Put"])
def update_student(id):

    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s", (name, age, course,id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Student added successfully"})

if __name__ == "__main__":
    app.run(debug=True)