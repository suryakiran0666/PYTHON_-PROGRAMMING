budget = float(input("Enter budget: "))
usage = float(input("Data required (GB): "))
days = int(input("Validity required (days): "))
plans = [
    ("Basic", 199, 2, 28, 50),
    ("Smart", 249, 3, 28, 50),
    ("Max", 299, 4, 56, 40)
]
best = None
for name, cost, data, valid, rate in plans:
    extra = max(0, usage - data) * rate
    total = cost + extra

    if valid >= days and total <= budget:
        if best is None or total < best[1]:
            best = (name, total, extra)
if best:
    print("\nMost Economical Plan:", best[0])
    print("Excess Charges:", best[2])
    print("Total Cost:", best[1])
else:
    print("No eligible plan found.")

