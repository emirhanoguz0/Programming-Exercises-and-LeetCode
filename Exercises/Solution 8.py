l = input().split(",")
x = int(l[0])
y = int(l[1])

l = [[i*j for i in range(y)] for j in range(x)]

print(l)