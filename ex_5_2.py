largest = None
smallest = None
while True:
    totalval = input('Enter a number:')
    if totalval == 'done':
        break
    else:
        try:
            intval = int(totalval)
        except:
            print('Invalid input')
            continue
    if largest is None or largest < intval:
        largest = intval
    if smallest is None or smallest > intval:
        smallest = intval
print("Maximum is", largest)
print("Minimum is", smallest)
