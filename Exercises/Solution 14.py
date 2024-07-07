l = list(input())

alphabet_l = 'abcdefghijklmnopqrstuvwxyz'
alphabet_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
UPPER_CASE = 0
LOWER_CASE = 0

for x in l:
    if x in alphabet_u:
        UPPER_CASE += 1
    elif x in alphabet_l:
        LOWER_CASE += 1

print("UPPER CASE", UPPER_CASE ," LOWER CASE", LOWER_CASE)
