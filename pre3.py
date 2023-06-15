import re

fname = 'regex_sum_ass.txt'
handle = open(fname)

numlist = list()

for line in handle:
    x = re.findall('[0-9]+', line)
    if len(x) > 1:
        for i in x:
            y = int(i)
            numlist.append(i)
print(sum(numlist))
