name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours_occ = {}
for line in handle:
    line = line.strip().split()

    if len(line) < 6 or line[0] != "From":
        continue

    time = line[5].split(":")
    hour = time[0]
    hours_occ[hour] = hours_occ.get(hour, 0) + 1

hours_occ_tuples = sorted([(key, value) for key, value in hours_occ.items()])
for hour, occ in hours_occ_tuples:
    print(hour, occ)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days.index('Mon'))