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

@app.route("/api/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "Student Deleted sucessfully"   
    })

if __name__ == "__main__":
    app.run(debug=True)