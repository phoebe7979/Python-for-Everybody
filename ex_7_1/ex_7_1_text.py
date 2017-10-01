fname = input('Enter file name:')
file = open(fname)
for line in file:
    clearline = line.strip()
    print(clearline.upper())
