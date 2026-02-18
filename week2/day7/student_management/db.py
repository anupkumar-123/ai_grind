import mysql.connector
from mysql.connector import Error

#--------------DATABASE CONFIQ-------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Password",
    "database": "student_management"
}

#--------------CONNECTION--------------------
def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print("Database connection error: ", e)
        return None
    
#-------------INITIALISE TABLES-----------------
def init_db():
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

# User table
    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS users (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(100) UNIQUE NOT NULL,
                   password VARCHAR(255) NOT NULL ) """)
    
    # STUDENT TABLE
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS students(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(100) NOT NULL,
                   age INT,
                   course VARCHAR(100))""")
    
    conn.commit()
    cursor.close()
    conn.close()