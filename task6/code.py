n = int(input("Passengers: "))
total = 0
for i in range(n):
    age = int(input("Age: "))
    d = float(input("Distance (km): "))
    c = input("Class (S/A): ").upper()
    cancel = input("Cancelled (y/n): ").lower()
    fare = d * (2 if c == "S" else 4)
    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.6
    fare += 20
    if cancel == "y":
        fare *= 0.5
    print("Fare:", round(fare, 2))
    total += fare
print("Total fare:", round(total, 2))

