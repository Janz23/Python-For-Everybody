fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = []

for line in fh:
    if not line.startswith("From:"):continue
    x = line.split()
    lst.append(x[1])
    count = count + 1

for i in lst:
    print(i)

print("There were", count, "lines in the file with From as the first word")
