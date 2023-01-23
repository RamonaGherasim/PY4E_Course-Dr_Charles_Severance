def compute_pay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = (40*r) + (h - 40) * 1.5 * r
    return pay


hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
p = compute_pay(hrs, rate)
print("Pay", p)
