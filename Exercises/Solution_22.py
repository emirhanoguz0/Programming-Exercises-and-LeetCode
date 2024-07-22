l = input().split(" ")
t = sorted(tuple(l))
d = {}

for c in t:
    d[c] = 0
for c in l:
    d[c] += 1

for x,y in d.items():
    print( f"{x}:{y}",end=" ")