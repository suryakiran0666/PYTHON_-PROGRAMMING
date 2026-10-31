bills = []
for m in range(3):
    u = int(input("Units: "))
    cost = min(u, 100)*2 + max(0, min(u-100, 100))*3 + max(0, u-200)*5
    bill = (cost + 50) * 1.05
    if u < 50:
        bill *= 0.9
    bills.append(bill)
    print("Bill:", round(bill, 2))
for i in range(1, 3):
    if bills[i] > bills[i-1] * 1.2:
        print("Unusual increase in month", i+1)

