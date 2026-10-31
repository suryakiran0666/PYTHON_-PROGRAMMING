c = float(input("Consultation: "))
d = float(input("Diagnostics: "))
t = float(input("Treatment: "))
p = float(input("Payment: "))
bill = c + d + t
if bill >= 5000:
    bill *= 0.9
print("Final Bill:", bill)
if p < 0:
    print("Invalid payment")
elif p >= bill:
    print("Paid")
else:
    print("Pending:", round(bill-p, 2))
