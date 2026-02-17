from services.student_service import(
    create_student,
    show_sudents,
    edit_student,
    remove_student
)

def menu():
    while True:
        print("\n=======STUDENT MANAGEMENT SYSTEM========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            show_sudents()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()