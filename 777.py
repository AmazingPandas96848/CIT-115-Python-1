# INPUT VALIDATION FUNCTIONS

def get_positive_float(prompt):
    while True:
        try:
            fltValue = float(input(prompt))
            if fltValue <= 0:
                print("Value must be a positive number.")
            else:
                return fltValue
        except ValueError:
            print("Please enter a numeric value.")

def get_non_negative_float(prompt):
    while True:
        try:
            fltValue = float(input(prompt))
            if fltValue < 0:
                print("Value cannot be negative.")
            else:
                return fltValue
        except ValueError:
            print("Please enter a numeric value.")

def get_positive_int(prompt):
    while True:
        try:
            intValue = int(input(prompt))
            if intValue <= 0:
                print("Value must be a positive integer.")
            else:
                return intValue
        except ValueError:
           print("Please enter a whole number.")

# USER INPUTS

fltDeposit = get_positive_float("Enter the initial deposit amount: $")
fltInterestRate = get_positive_float("Enter the annual interest rate (e.g., 4 for 4%): ")
intNumMonths = get_positive_int("Enter the number of months: ")
fltGoal = get_non_negative_float("Enter your savings goal amount (0 if none): $")

# CONVERSIONS

fltMonthlyRate = (fltInterestRate / 100) / 12  # Convert annual percentage to monthly decimal

# Compound Interest Calculation for Fixed Months

fltBalance = fltDeposit  # Reset balance for monthly tracking

print("\n--- Monthly Account Balances ---")
for intMonth in range(1, intNumMonths + 1):
    fltInterest = fltBalance * fltMonthlyRate
    fltBalance += fltInterest
    print(f"Month {intMonth}: ${fltBalance:,.2f}")

# Find Number of Months to Reach Goal

if fltGoal > 0:
    fltBalanceGoal = fltDeposit  # Reset for goal tracking
    intGoalMonths = 0

    while fltBalanceGoal < fltGoal:
        fltInterest = fltBalanceGoal * fltMonthlyRate
        fltBalanceGoal += fltInterest
        intGoalMonths += 1

    print(f"\nIt will take {intGoalMonths:,} months to reach your goal of ${fltGoal:,.2f}.")