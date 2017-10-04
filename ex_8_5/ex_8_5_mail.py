filename = input('Enter file name:')
fileopen = open(filename)
count = 0
for line in fileopen:
    linestrip = line.rstrip()
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        splitline = line.split()
        print(splitline[1])
        count = count + 1
    else:
        continue
print('There were', count ,'lines in the file with From as the first word')
