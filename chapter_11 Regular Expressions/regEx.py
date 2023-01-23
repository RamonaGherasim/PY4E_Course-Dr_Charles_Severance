import re

# Use this if want to read another file (such as regex_sum_42.txt)
# file = input("Enter file name: ")

file = 'regex_sum_1719379.txt'
handle = open(file)

results = []
for line in handle:
    line.strip()
    num = re.findall('([0-9]+)', line)
    if num:
        results.append(num)

sums = []
for i in results:
    sums.append((sum([int(j) for j in i])))

total = sum(sums)
print(total)

# Or cool short version for all of the above code
print(sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_1719379.txt')
                                      .read())]))
