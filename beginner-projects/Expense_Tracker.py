#Expense Tracker
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

    try:
        choice = int(input("Enter Choice\n"))
    except ValueError:
        print("Invalid Choice")
        continue

    if choice == 4:
        print("Goodbye")
        break

    if choice == 1:
        expense_name = input("Enter Expense Name\n")
        try:
            expense_amount = int(input("Enter Amount\n"))
            with open("expense.txt", "a") as f:
                f.write(f"{expense_name},{expense_amount}\n")
            print("Expenses added successfully!")
        except ValueError:
            print("Invalid Amount")

    elif choice == 2:
        try:
            with open("expense.txt", "r") as f:
                info = f.read()
                if info:
                    print(f"Expenses:\n{info}")
                else:
                    print("Expense not found")
        except FileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == 3:
        try:
            with open("expense.txt", "r") as f:
                lines = f.readlines()
                total = 0
                for line in lines:
                    if line.strip():
                        amount = int(line.split(",")[1])
                        total += amount
                print(f"Total Spent = {total}")
        except FileNotFoundError:
            print("No expenses recorded yet.")

                    
