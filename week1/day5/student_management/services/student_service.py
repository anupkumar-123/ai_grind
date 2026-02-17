from models.student_model import(
    add_student,
    get_all_students,
    update_student,
    delete_student
)

def create_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter course name: ")
    add_student(name, age, course)
    print("Student Added Successfully")

def show_sudents():
    students = get_all_students()
    print("\n Student List")
    for s in students:
        print(f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Course: {s[3]}")

def edit_student():
    student_id = int(input("Enter Student ID to update: "))
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    course = input("Enter new course: ")
    update_student(student_id, name, age, course)
    print("Student Updated Successfully")

def remove_student():
    student_id = int(input("Enter Student ID to update: "))
    delete_student(student_id)
    print("Student Deleted Successfully")

    


