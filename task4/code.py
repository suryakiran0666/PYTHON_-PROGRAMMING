
basic = float(input("Basic pay: "))
allow = float(input("Allowances: "))
ot = float(input("Overtime: "))
inc = float(input("Incentives: "))
gross = basic + allow + ot + inc
if gross <= 20000:
    tax = gross * 0.05
elif gross <= 50000:
    tax = 1000 + (gross - 20000) * 0.10
else:
    tax = 4000 + (gross - 50000) * 0.20
net = gross - tax
print("\n--- SALARY STATEMENT ---")
print("Gross Salary:", gross)
print("Deduction:", tax)
print("Net Salary:", net)

