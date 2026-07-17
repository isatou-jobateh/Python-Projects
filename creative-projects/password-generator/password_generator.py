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
        charater = random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        password = password + charater


    print(f"Your password is : {password}")

if __name__ =="__main__":
     password_generator()





  