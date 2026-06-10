def main():
    print("==== Expense Tracker ====")
    expenses = []

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show total expenses")
        print("4. Delete Expense")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("==== Add Expense ====")
            amount = add_expense()
            expenses.append(amount)
            print("\nExpense added successfully!\n")
        elif choice == 2:
            print("==== View Expenses ====")
            view_expenses(expenses)
            print("\n")
        elif choice == 3:
            print("==== Total Expenses ====")
            totalExpense = total_expenses(expenses)
            print(f"Total Expenses: ${totalExpense}")
            print("\n")
        elif choice == 4:
            print("==== Delete Expense ====")
            delete_expense(expenses)
        elif choice == 5:
            print("Exiting...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")
            


def add_expense():
    expense_name = input("Enter expense name: ")
    amount = int(input("Enter expense amount: "))
    return {"name": expense_name, "amount": amount}

def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['name']} - ${expense['amount']}")


def total_expenses(expenses):
    if not expenses:
        return 0
    return sum(expense['amount'] for expense in expenses)

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return
    
    view_expenses(expenses)
    choice = int(input("Enter the number of the expense to delete: "))
    if 1 <= choice <= len(expenses):
        deleted_expense = expenses.pop(choice - 1)
        print(f"Deleted expense: {deleted_expense['name']} - ${deleted_expense['amount']}")
    else:
        print("Invalid choice. Please try again.")

main()