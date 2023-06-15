import re

fname = 'regex_sum_ass.txt'
handle = open(fname)

numlist = list()

for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) !=1: continue
    num = int(x[0])
    numlist.append(num)


print("Sum of all:",sum(numlist))
