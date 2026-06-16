"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def print_report(incomes, numbers_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, numbers_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:.2f} -Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_of_months = int(input("How many months? "))

    for month in range(1, numbers_of_months + 1):
        income = float(input(f"Enter income for month {str(month)} :"))
        incomes.append(income)

    print_report(incomes, numbers_of_months)
main()