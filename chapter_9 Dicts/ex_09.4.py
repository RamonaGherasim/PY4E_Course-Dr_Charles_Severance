name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = {}
for line in handle:
    line = line.strip().split()

    if len(line) < 2 or line[0] != "From":
        continue

    email = line[1]
    di[email] = di.get(email, 0) + 1

max_commits = None
max_commits_email = None
for key, value in di.items():
    if max_commits is None or value > max_commits:
        max_commits = value
        max_commits_email = key

print(f'{max_commits_email} {max_commits}')