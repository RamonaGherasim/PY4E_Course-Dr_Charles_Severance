hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter rate: "))

if h <= 40:
    pay = h * rate
else:
    pay = (40*rate) + (h - 40) * 1.5 * rate

print(pay)