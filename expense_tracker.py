# Personal Expense Tracker

expenses = []

while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category (Food, Travel, Shopping, etc.): ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nExpense List")
            print("----------------------------")
            for expense in expenses:
                print(
                    f"Category: {expense['category']} | Amount: ₹{expense['amount']}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Expense: ₹{total}")

    elif choice == "4":
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
