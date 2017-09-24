# This is simliar to ex_3_1 but adds try and except
hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print("Error. Please enter numeric input.")
    quit()
rate = input("Enter Rates:")
try:
    r = float(rate)
except:
    print("Error. Please enter numeric input.")
    quit()
if h <= 40:
    print(h * r)
else:
    print((40 * r) + ((h - 40) * (1.5 * r)))
