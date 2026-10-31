m = float(input("Material cost: "))
l = float(input("Labour cost: "))
w = float(input("Wastage %: "))
mc = float(input("Machine cost: "))
s = float(input("Selling price per item: "))
q = int(input("Quantity: "))
t = float(input("Profit target: "))
cost = (m + l + mc + m*w/100) * q
profit = s*q - cost
print("Total Cost:", cost)
print("Profit:", profit)
print("Target Achieved" if profit >= t else "Target Not Achieved")
