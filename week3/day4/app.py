from flask import Flask, request, jsonify

from flask_jwt_extended import(
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import check_password_hash, generate_password_hash
import pymysql

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-key'

jwt = JWTManager(app)



def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Password",
        database="testdb",

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

@app.route("/login", methods=["POST"])
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
    
    access_token = create_access_token(identity={
        "username":user["username"],
        "role": user["role"]
    })
       

    return jsonify({
            "message" : "Login Successfully",
            "access_token": access_token
        }), 200
 
@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({
            "status": "error",
            "message": "Admin access required"
        }), 403
    
    return jsonify({
        "message": f"Welcome {current_user}",
        "status": "Access Granted"

    })

if __name__ == "__main__":
    app.run(debug=True)