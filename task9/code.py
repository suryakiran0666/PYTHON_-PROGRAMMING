budget = float(input("Budget: "))
rate = float(input("Exchange rate: "))
fee = float(input("Fee percentage: "))
expenses = {}
for c in ["Food", "Travel", "Hotel"]:
    x = float(input(c + " expense: "))
    expenses[c] = x * rate * (1 + fee / 100)
total = sum(expenses.values())
largest = max(expenses, key=expenses.get)
print("Total:", round(total, 2))
print("Largest:", largest)
print("Within Budget" if total <= budget else "Over Budget")
