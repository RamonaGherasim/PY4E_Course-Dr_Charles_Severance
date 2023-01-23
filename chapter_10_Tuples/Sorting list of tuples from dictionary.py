# Sorting Lists of Tuples
# Produce a list of tuples from a dictionary, and sort that list of tuples
# Now you can sort dictionary items!

# ===== Sorting by dict keys =====
dictionary = {'c': 10, 'z': 1, 'a': 22}
dict_items = dictionary.items()
sorted_dict_items = sorted(dict_items)
print(sorted_dict_items)

for key, value in sorted_dict_items:
    print(key, value)


# ===== Sorting by dict values =====
temp_list = []
for key, value in dict_items:
    temp_list.append((value, key))
print(temp_list)
sorted_temp_list = sorted(temp_list, reverse=True)
print(sorted_temp_list)

for value, key in sorted_temp_list:
    print(key, value)