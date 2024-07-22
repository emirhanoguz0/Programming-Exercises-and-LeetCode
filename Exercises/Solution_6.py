from math import*

C = 50
H = 30
l = input().split(",")

for D in l:
    print(int(sqrt(2*C*int(D)/H)))