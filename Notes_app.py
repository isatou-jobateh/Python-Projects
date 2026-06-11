
#Mini Project
#Notes App
print("1. View notes")
print("2. Add notes")
print("3. Exit")

while True:
	user_choice = input("Enter choice: ")

	if user_choice == "1":
		try:
			with open("notes.txt", "r") as f: 
				notes = f.read()
				if notes.strip(): 
					print("\nYour Notes:\n", notes)
				else:
					print("\nNo notes found.")
		except FileNotFoundError:
			print("\nNo notes found. Add some notes first.")
	elif user_choice == "2":
		note = input("Enter your note: ")
		with open("notes.txt", "a+") as f: #The plus sign tells Python: "Open this to append, but if the file doesn't exist yet, go ahead and create an empty one safely without crashing!"
			f.write(note + "\n")
		print("Note added successfully!")
	elif user_choice == "3":
		print("Goodbye!")
		break
	else:
		print("Invalid choice")
