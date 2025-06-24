
# EXception handling in generators
def count(firstval=0, step=1):
    counter = firstval
    while True:
        try:
            new_counter_val = yield counter  # Generator Pauses here
            # On Exception the following line will not be executed
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val
        except Exception:
            yield (firstval, step, counter)


c = count()
for i in range(6):
    print(next(c))
print("Let us see what the state of the iterator is:")
state_of_count = c.throw(Exception)
print(state_of_count)
print("now, we can continue:")
for i in range(3):
    print(next(c))
