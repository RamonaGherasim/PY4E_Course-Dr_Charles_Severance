fh = open('mbox-short.txt')

for line in fh:
    line = line.rstrip()
    print(line.upper())