#Mini Project
#Student Record System
# The student dictionary database
students = {
	"Aisha": 85,
	"Maya": 92
}

while True:
	print("\n--- Student Record System ---")
	print("1. View Students")
	print("2. Add Student")
	print("3. Search Student")
	print("4. Exit")
	
	choice = input("Enter choice (1-4): ")
	
	if choice == "1":
		# Check if the dictionary is empty first
		if not students:
			print("No student records found.")
		else:
			print("\n--- Student List ---")
			# Loop through keys (names) and values (grades)
			for name, grade in students.items():
				print(f"Name: {name} | Grade: {grade}")
		
	elif choice == "2":
		# Get separate inputs for the name and the grade
		name = input("Enter student name: ")
		grade = int(input("Enter student grade: ")) # Convert grade to a number
		
		# Add or update the key-value pair in the dictionary
		students[name] = grade
		print(f"Successfully added {name} with a grade of {grade}.")
		
	elif choice == "3":
		name = input("Enter student name to search: ")
		# Check if the name exists as a key in the dictionary
		if name in students:
			print(f"Found! {name}'s grade is {students[name]}.")
		else:
			print("Student not found.")
			
	elif choice == "4":
		print("Exiting system. Goodbye!")
		break # Breaks the while loop to safely close the program
		
	else:
		print("Invalid choice! Please choose a number between 1 and 4.")
