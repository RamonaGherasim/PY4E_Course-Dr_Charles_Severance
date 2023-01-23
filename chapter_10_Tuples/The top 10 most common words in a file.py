file_handle = open('romeo.txt')
words_count = {}

for line in file_handle:
    words_list = line.split()
    for word in words_list:
        words_count[word] = words_count.get(word, 0) + 1  # Using the IDIOM

# Expanded way
# tuples_list = []
# for key, value in words_count.items():
#     tuples_list.append((value, key))

"""
The above code in an even shorter version, using list comprehension
tuples_list = sorted([(value, key) for key, value in words_count.items()]))
"""
tuples_list = sorted([(value, key) for key, value in words_count.items()], reverse=True)

# tuples_list = sorted(tuples_list, reverse=True)
for value, key in tuples_list[:10]:  # To get the top 10 only
    print(key, value)


