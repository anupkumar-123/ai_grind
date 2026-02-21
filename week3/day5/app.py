from flask import Flask, request, jsonify, render_template

from flask_jwt_extended import(
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import check_password_hash, generate_password_hash
import pymysql
import mysql.connector

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-key'

jwt = JWTManager(app)



def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Password",
        database="ai_grind",

        cursorclass=pymysql.cursors.DictCursor
    )
@app.route("/register", methods=["POST"])
def register():
    
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    hashed_password = generate_password_hash(password)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"message": "User Registered successfully"})

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
   

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"message": "Invalid Credential"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"message" : "Invalid Credetial"}), 401
    
    access_token = create_access_token(identity=username)
       

    return jsonify({
            "message" : "Login Successfully",
            "access_token": access_token
        }), 200

@app.route("/api/students", methods=["GET"])
@jwt_required()
def protected_students():
    current_user = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({
        "user": current_user,
        "data": students
    })


@app.route("/frontend")
def frontend():
    return render_template("api_frontend.html")

if __name__ == "__main__":
    app.run(debug=True)