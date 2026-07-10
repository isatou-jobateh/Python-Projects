# To-Do-List File Version
while True:
    print("1. Add Task")
    print("2. view Task")
    print("3. Delete Task")
    print("4. Exit")

    try:
        user_choice = int(input("Enter choice \n"))
    except ValueError:
        print("Invaild choice")
        continue

    if user_choice == 4:
        print("Goodbye")
        break
    try:
        if user_choice == 1:
            tasks = input("Enter note\n")
            with open("task.txt", "a") as f:
                f.write(tasks)
                print("Task Added successfully!")

        elif user_choice == 2:
            with open("task.txt", "r") as f:
                content = f.readlines()
                for i , tasks in enumerate(content , start=1):
                    print(f"Notes : {i, tasks.strip()}")
                    
        elif user_choice == 3:
            with open("task.txt" ,"r") as f:
                tasks = f.readlines()
            del_task = int(input("What number do you want to delete\n"))
            tasks.pop(del_task -1)
            with open("task.txt","w") as f:
                f.writelines(tasks)
                print("Task deleted successfully!")
    except FileNotFoundError:
        print("File not found")
        break




