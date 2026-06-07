# def reverse_from_left(text):
#     if len(text) < 1:
#         return None
#     if len(text) == 1:
#         return text
    

#     return reverse_from_left(text[1::-1]) + text[-1]


# print(reverse_from_left("abcd"))






def reverse_from_left(text):
    if len(text) <= 1:
        return text
    
    return reverse_from_left(text[1:]) + text[0]

print(reverse_from_left("abcd"))

print("--------------")


def reverse_from_right(text):
    if len(text) <= 1:
        return text
    
    return text[-1] + reverse_from_right(text[:-1])

print(reverse_from_right("abcd"))