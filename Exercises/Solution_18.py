from re import*
l = input().split(",")

abc = []
alphabet = "[a-z]"
alphabetb = "[A-Z]"
nums = "[0-9]"
syms = "[$#@]"

for c in l:
    if len(c) > 12 or len(c) < 6:
        continue
    if not search(alphabet,c):
        continue
    elif not search(nums,c):
        continue
    elif not search(syms,c):
        continue
    elif not search(alphabetb,c):
        continue
    abc.append(c)

print(",".join(abc))