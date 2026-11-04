# Personal Expense & Budget Manager

## 1. Project Overview
The Personal Expense & Budget Manager is a Python-based application that helps users record their daily expenses and manage their monthly budget. It calculates total spending, remaining budget, and budget usage percentage.

## 2. Project Objectives
- To record daily expenses.
- To manage monthly budgets.
- To calculate total expenses.
- To track remaining budget.
- To display category-wise spending.
- To help users control unnecessary expenses.

## 3. Features
- Set a monthly budget.
- Add new expenses.
- Store expense records in a CSV file.
- Validate expense amount and date.
- Calculate total spending.
- Calculate remaining budget.
- Display budget usage percentage.
- Show warnings when the budget is nearly exhausted or exceeded.
- Display category-wise expenses.

## 4. Technologies Used
- Programming Language: Python
- Library: Pandas
- Data Storage: CSV
- Code Editor: Visual Studio Code

## 5. Requirements
- Python 3 installed.
- Pandas library installed.
- Visual Studio Code or another Python editor.

Install Pandas using:

```bash
python -m pip install pandas
```

## 6. Files Required
- `one.py` – Main Python program.
- `expenses.csv` – Stores expense records.
- `README.md` – Project documentation.

## 7. How to Execute the Project

1. Open the project folder in VS Code.
2. Open the terminal.
3. Install the required library:

```bash
python -m pip install pandas
```

4. Run the program:

```bash
python one.py
```

5. Follow the instructions displayed on the screen.

## 8. Input Details
The program accepts:
- Monthly budget.
- Expense date in YYYY-MM-DD format.
- Expense category.
- Expense amount.

## 9. Output Details
The program displays:
- Confirmation when an expense is saved.
- Total amount spent.
- Remaining monthly budget.
- Budget usage percentage.
- Budget warning messages.
- Category-wise expense details.

## 10. Testing
The project will be tested using the following test cases:

1. Normal Input – Set a valid monthly budget.
2. Boundary Input – Add an expense equal to the monthly budget.
3. Invalid Input – Enter a negative expense amount or an invalid date.
4. Different Valid Scenario – Add multiple expenses from different categories and check the final report.

Screenshots of the input and output for each test case are included in the project submission PDF.

## 11. Conclusion
The Personal Expense & Budget Manager provides a simple way to record expenses and monitor monthly spending. It helps users understand their spending habits and manage their budget effectively.