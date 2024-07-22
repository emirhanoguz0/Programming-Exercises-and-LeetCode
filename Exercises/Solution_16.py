numbers = input().split(",")
odd_numbers = [x for x in numbers if int(x)%2!=0]

print(",".join(odd_numbers))