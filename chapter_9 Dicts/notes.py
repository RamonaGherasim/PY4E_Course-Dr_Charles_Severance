counts = {'chuck': 1, 'annie': 42, 'jan': 100}
print(counts.get('jan', 0))

counts['tim'] = counts.get('tim', 0) + 1
print(counts.get('tim', 0)+1)

print(counts)