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

@app.route("/api/students", methods=["GET"])
def api_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close
    conn.close()

    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)
