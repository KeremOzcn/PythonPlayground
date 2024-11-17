def my_generator():
    # Defines a generator function.
    for i in range(3):
        yield i
        # Yields the next value in the sequence.

for value in my_generator():
    # Iterates through the values produced by the generator.
    print(value)
    # Prints each value.
