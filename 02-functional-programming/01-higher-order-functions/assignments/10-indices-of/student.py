# def is_palindrom(string):
#     return string == string[::1]


# def indices_of(xs, condition):
#     indices = []
#     for index, string in enumerate(xs):
#         if condition(string):
#             indices.append(index)
#     return indices



# print(indices_of(["kayak", "never", "rotator", "palindrome"], is_palindrom))




def indices_of(xs, condition):
    indices = []
    for index, string in enumerate(xs):
        if condition(string):
            indices.append(index)
    return indices


def is_palindrome(string):
    return string == string[::-1]


print(indices_of(["kayak", "never", "rotator", "palindrome"], is_palindrome))