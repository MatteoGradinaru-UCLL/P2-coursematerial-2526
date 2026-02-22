def find(lst, condition):
    for obj in lst:
        if condition(obj):
            return obj