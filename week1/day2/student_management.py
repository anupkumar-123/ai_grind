class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

class StudenClassManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter your course: ")
        student = Student(id, name, age, course)

        self.students.append(student)
        print("Student added successfully.")

    def view_student(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        id = input("Enter student ID to search: ")
        for student in self.students:
            if student.id == id:
                student.display()
                return
        print("Student not found.")

    def delete_student(self):
        id = input("Enter student ID to delete: ")
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def update_student(self):
        id = input("Enter student ID to update: ")
        for student in self.students:
            if student.id == id:
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                course = input("Enter new course: ")
                student.name = name
                student.age = age
                student.course = course
                print("Student updated successfully.")
                return
        print("Student not found.")

def main():
    manager = StudenClassManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_student()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.update_student()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        