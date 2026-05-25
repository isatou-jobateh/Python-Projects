#Student Grades System
grades = {
	"Aisha": 85,
	"Maya": 92,
	"John": 70
}
student_name = input()
if student_name in grades:
   print(grades[student_name])
else:
   print("student not found ")
