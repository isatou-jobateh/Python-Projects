# Password Generator
import random
import string

def password_generator():
    print("Welcome to generating your password")
    user = int(input("Enter password length: "))
 
    password = ""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    for i in range(user):
        first_password = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        second_password = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        third_password = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        fourth_password = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        fifth_password = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        sixth_password = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)

    password += first_password
    password += second_password
    password += third_password 
    password += fourth_password
    password += fifth_password
    password += sixth_password

    print(f"Your password is : {password}")

if __name__ =="__main__":
     password_generator()





  