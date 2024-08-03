class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generator(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

divisible_by_7 = DivisibleBySeven(50)
for num in divisible_by_7.generator():
    print(num)