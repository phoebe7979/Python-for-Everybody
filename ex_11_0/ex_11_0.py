import re
numberlist = list()
total = 0
# opening file
filename = input('Enter file name:')
if len(filename) < 1:
    filename = 'regex_sum_34535.txt'
filehand = open(filename)
# regular expression searching for all digits and make a list
for line in filehand:
    clearline = line.rstrip()
    number = re.findall('[0-9]+', line)
# combining all lists into single list
    if len(number) > 0:
        numberlist.extend(number)
# adding up all elements in a list after transforming them into integers
for n in numberlist:
    total = total + int(n)
# printing the sum
print(total)
