# Password Manager File Version
while True:
    print("1. Add Password")
    print("2. View Password")
    print("3. Search Password")
    print("4. Exit")
    try:
        users_choice = int(input("Enter Choice \n"))
    except ValueError:
        print("Invalid Choice")
        continue
    if users_choice == 4:
        print("Goodbye")
        break
    try:
        if users_choice == 1:
            name = input("Enter website name \n")
            password = input("Enter website's password\n")
            with open("password.txt", "a") as f:
                f.write(f"{name} , {password}\n")
            print("Name and Password added successfully!")

        elif users_choice == 2:
            with open("password.txt", "r") as f:
                content = f.read()
                if content:
                    print("Information found")
                    print(content)
                else:
                    print("No information found")

        elif users_choice == 3:
            query = input("Enter info to search\n")
            with open("password.txt", "r") as f:
                for line in f:
                    if query in line:
                        print("Information found")
                        print(line.strip())
                    else:
                     print("Information not found")
        else:
            print("Invalid Choice")
    except FileNotFoundError:
        print("File not found")
        continue 