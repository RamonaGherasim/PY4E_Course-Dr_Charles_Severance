fname = input("Enter file name: ")
fh = open(fname)

count = 0
addition = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    to_add = float(line[20:])
    count += 1
    addition += to_add

print(f"Average spam confidence: {addition/count}")