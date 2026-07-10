# To-Do-List using functions

def show_menu():
    print("\n==== To-Do List ====\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid choice. Please enter a number.")


def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_task(tasks):
    if not tasks:
        print("No task found")
        return
    print("Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")


def delete_task(tasks):
    if not tasks:
        print("No task found")
        return
    view_task(tasks)
    try:
        del_task = int(input("Enter the task number to delete: "))
        if 1 <= del_task <= len(tasks):
            tasks.pop(del_task - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


def main():
    tasks = []
    while True:
        choice = show_menu()
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


      
        

            


