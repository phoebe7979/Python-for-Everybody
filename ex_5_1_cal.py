num = 0
total = 0
avg = 0.0
while True:
    totalval = input('Enter a number:')
    try:
        if totalval == 'done':
            break
        else:
            floatval = float(totalval)
            num = num + floatval
            total = total + 1
            avg = num/total
    except:
        print('invalid value')
        continue
print(num, total, avg)
