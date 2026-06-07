def findMaximum(list):
    if len(list) == 0:
        raise IndexError("List is empty")

    if len(list) == 1:
        return list[0]
    
    if list[0] > findMaximum(list[1:]):
        return list[0]
    else:
        return findMaximum(list[1:])
