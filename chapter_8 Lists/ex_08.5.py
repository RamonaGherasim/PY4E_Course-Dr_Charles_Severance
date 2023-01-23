fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.strip().split()

    if len(line) < 2:
        continue

    if line[0] == "From":
        count += 1
        print(line[1])

print("There were", count, "lines in the file with From as the first word")
