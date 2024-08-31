class numbers_iter:
    def __init__(self, start):
        self.start_state = start
        self.state = start

    def __iter__(self):
        print("__iter__() called")
        return self

    def __next__(self):
        # example to show state updates, which are simple here
        prev_state = self.state
        next_state = self.state + 1
        self.state = next_state
        return prev_state

    def reset(self):
        self.state = self.start_state


n = numbers_iter(1)
print(f"type: {type(n)} iterator object: {iter(n)},type of iter object: {type(iter(n))}, Calling next: {next(n)}")

# iter() is implicitly called when we use for loop
# for i in iter(n):
for i in n:
    print(i)
    if i > 10:
        break

# iterator are not reset after the loop ends
for i in iter(n):
    print(i)
    if i > 12:
        break

print(f"Resetting numbers_iter {n.reset()}")  # functions that don't return anything return None by default
for i in n:
    print(i)
    if i > 10:
        break


# ----------------custom iterator----------------


class MyIterable:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return MyIterator(self.start, self.stop)


class MyIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += 1
            return f"value:{value}"
        else:
            raise StopIteration


for i in MyIterable(1, 10):
    print(i)


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
