def computepay(h,r):
	if h <= 40:
    	return(h * r)
	else:
    	return((40 * r) + ((h - 40) * (1.5 * r)))

hrs = input("Enter Hours:")
rph = input("Enter Rate:")
h = float(hrs)
r = float (rph)

p = computepay(h,r)

print(p)
