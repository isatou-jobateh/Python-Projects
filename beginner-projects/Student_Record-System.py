# Student Record System File Version
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        user_choice = int(input("Enter choice\n"))
    except ValueError:
        print("Invalid choice")
        continue

    if user_choice == 5:
        print("Goodbye!")
        break

    try:
        if user_choice == 1:
            students = input("Enter students info\n")
            with open("student.txt", "a") as f:
                f.write(students + "\n")
            print("Students info added successfully!")

        elif user_choice == 2:
                with open("student.txt", "r") as f:
                    info = f.read()
                    print(f"Students informations :{info}\n")      

        elif user_choice == 3:
            query = input("Enter student name or info to search\n")
            with open("student.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if query in line:
                            print(f"Sudent info found {line}")
                        else:
                             print("Student not found")

        elif user_choice == 4:
                with open("student.txt", "r") as f:
                    students = f.readlines()
                remove = input("Which student do you want  to delete:\n")
                students.pop()
                with open("student.txt", "w") as f:
                            f.writelines(students)
                            print("Student info deleted successfully!")
            
    except FileNotFoundError:
        print("File not found")
        break
