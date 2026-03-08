import json

expenses = []

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def menu():
    print("\n--- Smart Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Analysis")
    print("4. Highest Spending Category")
    print("5. Exit")


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/other): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")
    save_expenses()


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"Name: {exp['name']}, Amount: {exp['amount']}, Category: {exp['category']}")


def category_analysis():
    if not expenses:
        print("No expenses to analyze.")
        return

    summary = {}

    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']

    print("\n--- Category Wise Expenses ---")
    for cat, total in summary.items():
        print(f"{cat}: {total}")


def highest_category():
    if not expenses:
        print("No expenses to analyze.")
        return

    summary = {}

    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']

    top_cat = max(summary, key=summary.get)

    print(f"\nHighest Spending Category: {top_cat} - Amount: {summary[top_cat]}")


# Load saved expenses
load_expenses()

budget = float(input("Set your monthly budget: ").strip())


while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        add_expense()

        total = sum(exp['amount'] for exp in expenses)

        if total > budget:
            print("⚠️ Warning: You have exceeded your budget!")
        else:
            print(f"Total expenses so far: {total} / {budget}")

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        category_analysis()

    elif choice == '4':
        highest_category()

    elif choice == '5':
        print("Exiting.. Thank you!")
        break

    else:
        print("Invalid choice, try again.")