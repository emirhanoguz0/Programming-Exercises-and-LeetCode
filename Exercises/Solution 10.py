abc = input().split(" ")
l = []

for char in abc:
    if not char in l:
        l.append(char)

l = sorted(l)
print(" ".join(l))