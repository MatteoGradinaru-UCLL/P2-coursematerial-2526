# def repeat(value):
#     while True:
#         yield value

# iterator = repeat(5)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))




def repeat(value):
    while True:
        yield value


iterator = repeat(5)

print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 5