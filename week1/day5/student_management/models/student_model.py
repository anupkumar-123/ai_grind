from config.db_config import get_connection

def add_student(name, age, course):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(query, values)
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    return data

def update_student(student_id, name, age , course):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"

    cursor.execute(query, (name, age, course, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE id=%s"

    cursor.execute(query, (student_id,))
    conn.commit()
    conn.close()

