n = []
for i in range(1000,3001):
    s = str(i)
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
        n.append(s)

print(",".join(n))