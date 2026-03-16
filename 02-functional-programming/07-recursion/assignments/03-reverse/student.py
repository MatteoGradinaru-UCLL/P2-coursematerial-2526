def reverse_from_left(text):
    if len(text) < 1:
        return None
    if len(text) == 1:
        return text
    

    return reverse_from_left(text[1::-1]) + text[-1]


print(reverse_from_left("abcd"))