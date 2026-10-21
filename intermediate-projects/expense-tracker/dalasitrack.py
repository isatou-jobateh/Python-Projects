## Expense Tracker

import os

# File path for expenses.txt 
EXPENSES_FILE = os.path.join(os.path.dirname(__file__), "expenses.txt")

# Default sample expenses
default_expenses = [
     {"name": "CashPower", "category": "Electricity", "amount": 2500},
     {"name": "Rice", "category": "Food Staples", "amount": 4000},
     {"name": "Cooking Gas", "category": "Utility", "amount": 1400}
]

# Load expenses from file if it exists
expenses = []
if os.path.exists(EXPENSES_FILE):
     with open(EXPENSES_FILE, "r") as f:
          for line in f:
               parts = line.strip().split(",")
               if len(parts) == 3:
                    name, category, amount = parts
                    try:
                         expenses.append({"name": name, "category": category, "amount": int(amount)})
                    except ValueError:
                         continue
else:
     expenses = default_expenses.copy()

title = "Expense Tracker"

header = title.center(80, "=")
print(header)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Largest Expense")
    print("6. Set Budget")
    print("7. Search Expenses")
    print("8. Filter Expenses by Category")
    print("9. Save and Exit")

    choice = input("\n Enter your choice (1-9): ")
    if choice =="1":
        name = input("Enter expense name: ")
        category = input("Enter expense category: ")
        amount = (input(f"Enter amount spent on {category}: "))
        expenses.append({"name": name, "category": category, "amount": int(amount)})
        print("Expense Added")

    elif choice == "2":
        print("\nExpenses:")
        for expense in expenses:
            print(f"{expense['name']}: {expense['category']} : D{expense['amount']}")

    elif choice =="3":
            total = sum(expense["amount"]for expense in expenses)
            print(f"Total spending: D{total}")

    elif choice == "4":
         totals = {}
         for expense in expenses:
              cat = expense["category"]
              totals[cat] = totals.get(cat, 0) + expense["amount"]

         print("\n Spending by category: \n")
         for cat, amount in totals.items():
              print(f"{cat}: D{amount}")

    elif choice == "5":
         if not expenses:
              print("NO expenses yet")
         else:
              largest = max(expenses, key=lambda e: e["amount"])
              print(f"\nLargest expense: {largest['name']} ({largest['category']}): D{largest['amount']}")

    elif choice == "6":
         budget = int(input("Enter your budget: "))
         total_spending = sum(expense["amount"] for expense in expenses)
         if total_spending > budget:
            print(f"You have exceeded your budget of D{budget} by D{total_spending - budget}")
         else:
             print(f"Amount spent : D{total_spending} \n Remaining amount: D{budget - total_spending}")

    elif choice == "7":
         term = input("Search by name : ")
         results = [e for e in expenses if term in e ["name"]]
         if results:
              for e in results:
                   print(f"{e['name']}: {e['category']}: D{e['amount']}")
         else:
              print("No match found.")

    elif choice == "8":
         category = input("Enter category to filter by:")
         filtered = [e for e in expenses if e["category"] == category]
         if filtered:
              for e in filtered:
                   print(f"{e['name']}: {e['category']}: D{e['amount']}")
              print(f"Subtotal for {category}: D{sum(e['amount'] for e in filtered)}")
         else:
          print(f"No expenses found for category: {category}")

    elif choice == "9":
          with open(EXPENSES_FILE, "w") as f:
               for expense in expenses:
                    f.write(f"{expense['name']},{expense['category']},{expense['amount']}\n")
          print("Expenses saved to expenses.txt. Exiting program.")
          break
    
