fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "clown.txt"

hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()

    for word in words:
        """
        # One way (long way) of doing this:
        
        if word in di:
            di[word] += 1
        else:
            di[word] = 1

        # Combining teh above 4 lines in a short single contraction
        # Using .get()
        # If key not is not there, the count is zero (default)
        
        oldcount = di.get(word, 0)
        print(word, 'old', oldcount)
        newcount = oldcount + 1
        di[word] = newcount
        print(word, 'new', newcount)
        """

        # All of the above can be translated into the below line
        # This is an IDIOM: retrieve/create/update counter, all in one line
        di[word] = di.get(word, 0) + 1

print(di)

# Now I want to find the most common word

largest = -1
largest_key = None
for key, value in di.items():
    if value > largest:
        largest = value
        largest_key = key  # capture and remember the key that was largest

print(f'The word "{largest_key}" had a max count of {largest}')
