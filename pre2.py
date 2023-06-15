import re

fname = 'regex_sum_ass.txt'
handle = open(fname)

numlist = list()

for line in handle:
    x = re.findall('[0-9]+', line)
    if len(x) == 0: continue
    elif len(x) == 1:
        for y in x:
            j = int(y)
            numlist.append(j)
    elif len(x) > 1:
        for nuum in x:
            i = int(nuum)
            numlist.append(i)

print(sum(numlist))
