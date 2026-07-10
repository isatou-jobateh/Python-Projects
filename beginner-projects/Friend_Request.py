# friendship request
def be_my_friend(name = "Guest"):
    print(f"Hello my name is", name)
    print(f" Will you like to be my friend")
    choice = input()
    if choice == "yes":
        print("Yay! I'm so happy to have a new friend!")
    else:
        print("Oh thtat's okay")
    name = input("what's is your name?")
    print(f"{name} is a great name!")
    print("nice to meet you ")
   
be_my_friend("Aisha")