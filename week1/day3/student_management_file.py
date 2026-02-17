import json
import os

FILE_NAME = "students.json"

#-------------File Handling Function--------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return[]
    with open (FILE_NAME, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

#-------------CRUD Operation------------
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Nmae: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course" : course
    }
    data.append(student)
    save_data(data)
    print("Student added successfully")

def view_students():
    data = load_data()
    if not data:
        print("No student found")
        return
    for student in data:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    print()

def update_student():
    data = load_data()
    roll = input("Enter roll number to update: ")

    for student in data:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")
            save_data(data)
            print("Student updated successfully")
            return
    print("Student not found")

def delete_student():
    data = load_data()
    roll = input("Enter roll number to delete: ")

    for student in data:
        if student["roll"] == roll:
            data.remove(student)
            save_data(data)
            print("Student deleted successfully")
            return
    print("Student not found")

#-------------Main Menu-------------
while True:
    print("========Student Management System========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exit")
        break
    else: 
        print("Invalid choice, please try again")



                   

    