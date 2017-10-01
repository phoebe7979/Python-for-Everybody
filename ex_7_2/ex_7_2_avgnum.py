fname = input('Enter file name:')
fileopen = open(fname)
count = 0
totalnum = 0
for line in fileopen:
    if line.startswith('X-DSPAM-Confidence:'):
        locate = line.find(':')
        aftercolon = line[locate+1:]
        num = aftercolon.strip()
        floatnum = float(num)
        totalnum = totalnum + floatnum
        count = count + 1
    else:
        continue
avgfloatnum = totalnum/count
print('Average spam confidence:', avgfloatnum)
