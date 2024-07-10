l = input().split(" ")
sum = 0

for i in range(len(l)):
    if l[i] == "D":
       sum += int(l[i+1])
    elif l[i] == "W":
        sum -= int(l[i+1])

print(sum)