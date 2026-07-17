# Echoes of Time

title = "ECHOES OF TIME"

header = title.center(80, "=")
print(header)

import random

def welcome():
    print("Location : Magic Laboratory")
    print()
    print("Welcome , Time Traveler!")
    print()
    print("You have entered the Magic Laboratory , created by the brilliant scientist Dr. A. Jobateh")
    print()
    print("In the center of the room stands a mysterious machine known as the Time Tube ")
    print()
    print("Suddenly.....")
    print()
    print("The machine begins to glow")
    print()
    print("A hologram appears")
    print()
    print("Aurabee:")
    print("'warning...'")
    print("'Timeline corruption detected.'")
    print("'The four Time Crystals have scattered across history.'")
    print("'Only you can recover them.'")
    print()

def intro():
    pass

def meet_aurabee():
    pass

def ancient_egypt():
    pass

def medieval_kingdom():
    pass

def future_city():
    pass

def main():
    welcome()
    lives = 3
    time_crystal = 0
    user = input("Press Enter to begin your adventure.....")
    print()

    title_2 = "INTRO"
    header_2 = title_2.center(80, "=")
    print(header_2)
    intro()
    print()
    print("'Years ago, the brillint scientist Dr. A. Jobateh invented the Time Tube  to study history'")
    print("'During the  final experiment , four Time Crystals shatterd across history , causing the timeline to collapse.'" )
    print("'Before disappearing , Dr. A. Jobateh left one final message ..... '")
    print()
    meet_aurabee()
    print("'Meet Aurabee , Your AI assistant'")
    print()
    print("A hologram slowly appears")
    print()
    print("Aurabee: :")
    print("Geeting , Time Traveler.")
    print()
    user_name = input(" What's your name :")
    print()
    print(f"Welcome : {user_name}")
    print()
    print("From this moment forward , you are the Guardian of Time.")
    print()
    print("You have 3 lives.")
    print()
    print("You must recover the four Time Crystals before history disappears forver.")
    print()
    input("Press Enter to begin your first mission....")
    print()

    title_3 = "WELCOME TO ANCIENT EGYPT"
    header_3 = title_3.center(80, "=")
    print(header_3)
    print()
    ancient_egypt()
    print("Chapter 1")
    print("The Pyramid's Secret")
    print()
    print("Year : 2560 BC")
    print()
    print("Location : Ancient Egypt")
    print()
    print("The Time Tube lands beside the Great Pyramid")
    print()
    print("Workers are running everywhere")
    print()
    print("Someone shouts: ")
    print()
    print("'The pyramid cannot be compeleted!'")
    print()
    print("Aurabee :")
    print("A clue is hidden inside....")
    print()
    input("Press Enter to start ")
    print()
    print("Puzzle 1 - The Pharaoh's Riddle")
    print()
    print("'Rules: You have 3 attempts if you answer correctly you will be awared with your first Time Crystal.'")
    print("'But if all attemps are used you lose a live'")
    print()
    print("A mysterious old priest approaches you.")
    print("Priest:")
    print("'Only those with wisdom may enter the Great Pyramid.'")
    print()
    print("'You must answer my riddle'")
    print("My riddle is: ")
    print()
    print("'I speak without a mouth and hear without ears.'")
    print("'I have no body , but i come alive with the wind.'")
    print()
    print("What am I?")
    answer = "echo"
    attempts_allowed = 3
    for attempt in range(1, attempts_allowed + 1):
        guess = input(f"Enter your attempt {attempt}: ").strip().lower()
        if guess == answer:
            print("You got it right")
            print("You have been awarded your first Time Crystal")
            time_crystal = time_crystal + 1
            break
        else:
            remaining = attempts_allowed - attempt
            if remaining > 0:
                print(f"Incorrect. You have {remaining} attempts left.")
            else:
                print("All attempts are used.")
                print("You have lost 1 life")
                lives = lives - 1
                print("Continue the adventure")
    print()

    title_4 = "WELCOME TO MEDIEVAL KINGDOM"
    header_4 = title_4.center(80, "=")
    print(header_4)
    print()
    medieval_kingdom()
    print("Chapter 2")
    print("The King's Trial")
    print()
    print("The Time Tube begins to glow")
    print()
    print("A bright blue light surrounds you.")
    print()
    print(".....")
    print()
    print("Destination : Medieval Kingdom")
    print()
    print("Year : 1287")
    print()
    print("You arrive outside a huge castle")
    print()
    print("Knight rush past you")
    print()
    print("A guard blocks your path")
    print()
    print("Guard:")
    print("'No one may enter the castle without proving thier wisdom.'")
    print()
    print("Aurabee:")
    print("'The second Time Crystal is inside the castle'")
    print("'The Kings's adviser loves logic'")
    print("'prepare yourself.....'")
    print()
    input("Press Enter to start :")
    print()
    print("Puzzle 2 - The King's Trial")
    print()
    print("The king's adviser points to three ancient treasure chests.")
    print()
    print("Only one contains the Second Time Crystal.")
    print("Choose wisely....")
    print()
    print("1. Gold Chest")
    print("2. Silver Chest")
    print("3. Wooden Chest")
    print()
    choice = input("Choose a chest (1-3): ")
    try:
        choice_num = int(choice)
    except ValueError:
        print("Invalid choice. You lose one life.")
        choice_num = None
        lives -= 1

    correct = random.choice([1,2,3])
    if choice_num == correct:
        print("The chest slowly opens...")
        print()
        print(f"Inside is the {['','Gold Chest','Silver Chest','Wooden Chest'][correct]}")
        print()
        print("Aurabee:")
        print("Excellent work , Time Traveler")
        print()
        time_crystal = time_crystal + 1
    elif choice_num != correct:
        print("The chest is empty.")
        print()
        print("The guard shakes his head.")
        print()
        print("You lose one life ")
        lives = lives - 1
        if lives <= 0:
            print("You are out of lives : Game Over")
    print()

    title_5 = "WELCOME TO FUTURE CITY"
    header_5 = title_5.center(80, "=")
    print(header_5)
    print()
    future_city()
    print("Final Chapter")
    print("The Broken Timeline")
    print()
    print("The Time Tube begins to shake violently...")
    print()
    print("Aurabee:")
    print("'The timeline is collapsing!'")
    print()
    print("'One final challenge remains'")
    print()
    print("'Answer correctly , and history will be restored'")
    print()
    print("'Fail...'")
    print()
    print("'and time will be lost forever'")
    print()
    input("Press Enter to start")
    print()
    print("Final Puzzle- The Broken Timeline")
    print()
    print("Rules:")
    print("Aurabee will ask 3 questions about the journey you are about to complete.")
    print("If you answer all correctly you restore the timeline and win.")
    print("If you have 0 life left the time will be lost forever.")
    print()

    questions = [
        {
            "question": "Where did your adventure begin?",
            "choices": [
                "a) The Magic Laboratory",
                "b) The King's Castle",
                "c) The Great Pyramid",
            ],
            "answer": "a",
        },
        {
            "question": "What is the name of the AI that guided you?",
            "choices": [
                "a) Aurora",
                "b) Aurabee",
                "c) Atlas",
            ],
            "answer": "b",
        },
        {
            "question": "What powers the Time Tube",
            "choices": [
                "a) Magic Keys",
                "b) Time Crystals",
                "c) Gold Coins",
            ],
            "answer": "b",
        },
    ]

    all_correct = True
    for question in questions:
        print(question["question"])
        print()
        for choice in question["choices"]:
            print(choice)
            print()
        user_answer = input("Enter Choice: ").strip().lower()
        if user_answer == question["answer"]:
            print("Correct!")
            print()
            time_crystal += 1
        else:
            print("Incorrect.")
            print()
            all_correct = False
            lives -= 1
            if lives <= 0:
                print("You are out of lives : Game Over")
                print()
                break
            else:
                print(f"Lives remaining: {lives}")
                print()

    if all_correct and lives > 0:
        print("The Time Crystals begin to glow...")
        print()
        print("The Time Tube stabilizes")
        print()
        print("History repairs itself.")
        print()
        print("Aurabee:")
        print("Congratulations, Guardian of Time.")
        print()
        print("You have restored the timeline.")
        print()
        print("Dr. A. Jobateh would be proud")
        print()
        print("THE END")
    else:
        print("Game Over")

    print(f"Number of lives left: {lives}")
    print(f"How many Time Crystals collected: {time_crystal}")

    
    while True:
        print()
        print("Would you like to play again?")
        yes = input("Enter 'yes' or 'no': ").strip().lower()
        if yes == "yes":
            print()
            main()
            return
        elif yes == "no":
            print("Thank You for playing")
            return
        else:
            print("Please enter 'yes' or 'no'.")

    

if __name__ == "__main__":
    main()
