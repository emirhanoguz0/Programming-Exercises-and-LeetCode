import string

l = list(input())
digits=0
letters=0
alphabet=list(string.ascii_lowercase)
for x in l:
    if x in '0123456789':
        digits += 1
    elif x in alphabet:
        letters += 1

print("LETTERS ",letters,"DIGITS ",digits)