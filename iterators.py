class numbers_iter:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return self.start - 1


n = numbers_iter(1)
print(next(n))

for i in n:
    print(i)
    if i > 10:
        break

# numbers using generator


def numbers_gen(start):
    while True:
        yield start
        start += 1


# numbers_gen(1) returns a generator object
# next(gen) returns the next value from the generator objec
gen = numbers_gen(1)
print(numbers_gen(1))
for i in range(1, 11):
    print(next(gen))
