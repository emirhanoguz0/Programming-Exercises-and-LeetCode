def binary_to_integer(bi):
    num = 0
    num += int(bi[0]) * 8
    num += int(bi[1]) * 4
    num += int(bi[2]) * 2
    num += int(bi[3]) * 1
    return num

binaries = input().split(",")
integers = [0] * 4
d = []

for i in range(len(binaries)):
     integers[i] = binary_to_integer(binaries[i])
     if integers[i] % 5 == 0:
         d.append(binaries[i])

print(",".join(d))