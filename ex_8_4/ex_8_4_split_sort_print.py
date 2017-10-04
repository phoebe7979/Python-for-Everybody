filename = input('Enter file name:')
file = open(filename)
wordlist = list()
for line in file:
    eachline = line.rstrip()
    eachword = eachline.split()
    for x in eachword:
        if x not in wordlist:
            wordlist.append(x)
        else:
            continue
wordlist.sort()
print(wordlist)
