filename = input('Enter file name:')
fileopen = open(filename)
count = 0
for line in fileopen:
    linestrip = line.rstrip()
    words = linestrip.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    if words[0] == 'From':
        print(words[1])
        count = count + 1
print('There were', count ,'lines in the file with From as the first word')
