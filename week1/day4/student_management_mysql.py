import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="ai_grind"

    )
    return connection

def add_student(name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(query, values)
    conn.commit()

    print("Student added Successfully")
    cursor.close()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n Student List: ")
    for student in students:
        print(student)

    cursor.close()
    conn.close()

def update_student(student_id, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    query = """UPDATE students 
    SET name=%s, age=%s, course=%s
    WHERE id=%s
    """
    values = (name, age, course, student_id)
    cursor.execute(query, values)
    conn.commit()

    print("Student update successfully")

    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student deleted successfullyt")
    cursor.close()
    conn.close()

while True:
    print("\n========Student Management System==========")
    print("1. Add student")
    print("2. view students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter age: ")
        course = input("Enter course name: ")
        add_student(name, age, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")
        update_student(student_id, name, age, course)

    elif choice == "4":
        student_id = int(input("Enter Student ID: "))
        delete_student(student_id)

    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice")


