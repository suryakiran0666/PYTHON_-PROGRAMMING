v = float(input("Venue: "))
e = float(input("Equipment: "))
c = float(input("Catering: "))
t = float(input("Transport: "))
cert = float(input("Certificates: "))
s = float(input("Sponsorship: "))
fee = float(input("Registration fee: "))
cost = v + e + c + t + cert
short = max(0, cost - s)
n = int(short / fee) + (short % fee > 0) if fee > 0 else 0
print("Total Cost:", cost)
print("Sponsorship Shortfall:", short)
print("Break-even Registrations:", n)
