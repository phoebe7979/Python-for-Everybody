filename = input('Enter file name:')
openfile = open(filename)
fulllist = list()
dic = dict()
aaa = None
bbb = None
for line in openfile:
    completeline = line.rstrip()
    part = completeline.split()
    if len(part) < 2 or part[0] != 'From':
        continue
    if part[0] == 'From':
        fulllist.append(part[1])
for item in fulllist:
    dic[item] = dic.get(item,0) + 1
for key in dic:
    if dic[key] > bbb:
        aaa = key
        bbb = dic[key]
        print(aaa , bbb)
    else:
        continue
print(aaa , bbb)
