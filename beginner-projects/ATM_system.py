#Mini Project
#Mini ATM System 
balance = 1000 

while True: 
    print("1. Check Balance") 
    print("2. Deposit") 
    print("3. Withdraw") 
    print("4. Exit") 
    
    user_choice = int(input("Enter choice: ")) 
    
    if user_choice == 1: 
        print(f"Your balance is: {balance}") 
        
    elif user_choice == 2: 
        deposit_amount = int(input("Enter deposit amount: ")) 
        balance += deposit_amount
        print(f"Deposited successfully. New balance: {balance}") 
        
    elif user_choice == 3: 
        withdraw_amount = int(input("Enter withdrawal amount: ")) 
        if balance >= withdraw_amount: 
            balance -= withdraw_amount
            print(f"Withdrawal successful. Remaining balance: {balance}") 
        else: 
            print("Insufficient funds")
            
    elif user_choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select 1-4.")
