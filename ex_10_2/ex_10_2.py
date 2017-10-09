hourlist = list()
hourdic = dict()
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    completeline = line.rstrip()
    part = completeline.split()
    if len(part) < 2 or part[0] != 'From':
        continue
    if part[0] == 'From':
        time = part[5].split(':')
        hourlist.append(time[0])
for hour in hourlist:
    hourdic[hour] = hourdic.get(hour,0) + 1
hourcountlist = list()
for key, val in list(hourdic.items()):
    hourcountlist.append((key,val))
hourcountlist.sort()
for key,val in hourcountlist:
    print(key,val)
