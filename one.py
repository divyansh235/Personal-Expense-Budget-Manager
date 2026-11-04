import csv
import os
from datetime import datetime

import pandas as pd

# File used to store expenses
FILE_NAME = "expenses.csv"

# Monthly budget
monthly_budget = 0.0

# CSV file columns
COLUMNS = ["Date", "Category", "Amount"]


# 1. Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)


# 2. Read expenses from CSV using Pandas
def read_expenses():
    create_file()

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            return pd.DataFrame(columns=COLUMNS)

        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
        df = df.dropna(subset=["Amount", "Date", "Category"])
        df["Category"] = df["Category"].astype(str).str.strip()
        df = df[df["Category"] != ""]

        return df

    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=COLUMNS)


# 3. Set monthly budget
def set_budget():
    global monthly_budget

    try:
        amount = float(input("Enter your monthly budget: ₹"))

        if amount <= 0:
            print("Invalid budget. Amount must be positive.")
            return

        monthly_budget = amount
        print(f"Monthly budget set: {monthly_budget:.2f}")

    except ValueError:
        print("Invalid input. Please enter a number.")


# 4. Add a new expense
def add_expense():
    print("\n--- Add Expense ---")

    # Validate date format
    date_text = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    # Validate category
    category = input("Enter category (e.g. Food, Travel): ").strip()

    if not category:
        print("Invalid category. Category cannot be empty.")
        return

    # Validate expense amount
    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Invalid amount. Amount must be a positive number.")
            print("Expense not saved.")
            return

    except ValueError:
        print("Invalid amount. Please enter a number.")
        print("Expense not saved.")
        return

    # Save expense in CSV
    create_file()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date_text, category, amount])

    print("Expense saved.")

    # Show updated spending and budget status
    show_budget_status()


# 5. Calculate spending and remaining budget
def show_budget_status():
    df = read_expenses()
    total_spent = df["Amount"].sum()

    print(f"Total spent: {total_spent:.2f}")

    if monthly_budget <= 0:
        print("Set your monthly budget to track the remaining amount.")
        return

    remaining = monthly_budget - total_spent
    percentage = (total_spent / monthly_budget) * 100

    print(f"Remaining: {remaining:.2f}")
    print(f"Budget used: {percentage:.2f}%")

    
    if percentage > 100:
        print("Budget exceeded!")

    elif percentage == 100:
        print("Budget fully used (100%).")

    elif percentage >= 80:
        print("Warning: 80% or more of the budget is used.")



# 6. Show category-wise spending using groupby()
def category_summary():
    df = read_expenses()

    if df.empty:
        print("No expenses recorded yet.")
        return

    summary = df.groupby("Category")["Amount"].sum()

    print("\n--- Category-wise Spending ---")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


# 7. Display full expense report
def expense_report():
    df = read_expenses()

    print("\n--- Personal Expense & Budget Report ---")

    if df.empty:
        print("No expenses recorded yet.")
        show_budget_status()
        return

    print("\nAll Expenses:")
    print(df.to_string(index=False))

    print("\nCategory-wise Summary:")
    print(
        df.groupby("Category")["Amount"]
        .sum()
        .to_string()
    )

    print()
    show_budget_status()


# 8. Main menu
def main():
    create_file()

    while True:
        print("\n===================================")
        print(" PERSONAL EXPENSE & BUDGET MANAGER")
        print("===================================")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. Category-wise Summary")
        print("4. Expense Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            set_budget()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            expense_report()

        elif choice == "5":
            print("Thank you for using the Budget Manager!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Start the project
if __name__ == "__main__":
    main()
