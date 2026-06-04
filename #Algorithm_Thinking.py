#Algorithm Thinking
#Largest and Smallest
list = [7, 2, 15, 1, 9]
largest = list[0]
smallest = list[0]
for num in list:
	if num > largest:
	   largest = num
	if num < smallest:
	   smallest = num
print(f"largest = {largest} ,smallest = {smallest }")
