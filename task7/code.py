n = int(input("Number of products: "))
subtotal = tax = 0
for i in range(n):
    name = input("Product: ")
    cat = input("Category (F/E): ").upper()
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    amount = price * qty
    rate = 0.05 if cat == "F" else 0.18
    t = amount * rate
    subtotal += amount
    tax += t
    print(name, "Amount:", amount, "Tax:", round(t, 2))
discount = min(subtotal * 0.10, 200) if subtotal >= 1000 else 0
total = subtotal + tax - discount
print("Subtotal:", subtotal)
print("Tax:", round(tax, 2))
print("Discount:", round(discount, 2))
print("Final Bill:", round(total, 2))
