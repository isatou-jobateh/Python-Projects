# Mini Login Database (Dictionary Upgrade)
users = {"aisha": "1234", "maya": "abcd"}

username = input("Enter username: ")

if username in users:
    password = input("Enter password: ")
    if users[username] == password:
        print("Login successful!")
    else:
        print("Login unsuccessful.")
else:
    print("Username not found.")

