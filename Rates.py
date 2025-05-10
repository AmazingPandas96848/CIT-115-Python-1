# ASK USER FOR RATES AND TERMS
PV = float(input("Enter the principal investemnt:"))
R = float(input("Enter the annual interest rate:")) /100
T = float(input("How many times per year is the interest compounded: "))
M = float(input("For how many years will the account earn interest: "))

# FORMULA FOR INTEREST RATES
FV = PV * (1 + R / T) ** ( M * T)

# DISPLAY THE RESULT
print(f"Future value : ${FV:.2f}")
