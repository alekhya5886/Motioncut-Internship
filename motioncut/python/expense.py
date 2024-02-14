import json
import datetime

# Initialize expenses data
expenses = []

def load_expenses():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=2)

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. View Category-wise Expenditure")
    print("4. Exit")

def add_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def view_monthly_summary():
    month = input("Enter the month (MM): ")
    year = input("Enter the year (YYYY): ")

    total_expenses = 0
    for expense in expenses:
        expense_date = datetime.datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S")
        if expense_date.month == int(month) and expense_date.year == int(year):
            total_expenses += expense['amount']

    print(f"Total expenses for {month}-{year}: ${total_expenses:.2f}")

def view_category_wise_expenditure():
    category = input("Enter the expense category to view expenditure: ")

    total_expenses = 0
    for expense in expenses:
        if expense['category'].lower() == category.lower():
            total_expenses += expense['amount']

    print(f"Total expenditure for {category}: ${total_expenses:.2f}")

def main():
    load_expenses()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_monthly_summary()
        elif choice == '3':
            view_category_wise_expenditure()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()