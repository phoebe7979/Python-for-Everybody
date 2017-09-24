# Goal is to set 1x hourly rate when below 40 hrs and 1.5x hourly rate when
# above 40 hours.
hrs = input("Enter Hours:")
rate = input("Enter Rates:")
r = float(rate)
h = float(hrs)
if h <= 40:
    print(h * r)
else:
    print((40 * r) + ((h - 40) * (1.5 * r)))
