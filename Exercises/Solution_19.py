l = input().split(" ")
a = []

for x in l:
    a.append(tuple(x.split(",")))

a.sort(key=lambda x: x[0])
print(a)