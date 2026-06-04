import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "expenses.json"


def load_expenses():
    """Read expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    expenses = load_expenses()

    print("\nAdd Expense")
    title = input("Enter expense title: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    print("\nAll Expenses")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Title    : {expense['title']}")
        print(f"Category : {expense['category']}")
        print(f"Amount   : Rs. {expense['amount']:.2f}")
        print(f"Date     : {expense['date']}")


def delete_expense():
    expenses = load_expenses()

    if len(expenses) == 0:
        print("\nNo expenses to delete.")
        return

    view_expenses()

    try:
        expense_number = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if expense_number < 1 or expense_number > len(expenses):
        print("Invalid expense number.")
        return

    removed_expense = expenses.pop(expense_number - 1)
    save_expenses(expenses)
    print(f"Deleted expense: {removed_expense['title']}")


def calculate_total_spending():
    expenses = load_expenses()
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: Rs. {total:.2f}")


def show_menu():
    print("\n==============================")
    print("      Expense Tracker Menu")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Calculate Total Spending")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            calculate_total_spending()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
