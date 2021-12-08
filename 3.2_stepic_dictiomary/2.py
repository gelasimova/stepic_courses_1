d = input().lower().split()
dict = {}
for i in d:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for v, c in dict.items():
    print("{} {}".format(v, c))