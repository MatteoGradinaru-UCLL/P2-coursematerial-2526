# def partition(lst, condition):
#     lst1= []
#     lst2 =[]

#     for obj in lst:
#         if condition(obj):
#             lst1.append(obj)
#         else:
#             lst2.append(obj)
#     return lst1, lst2




def partition(lst, condition):
    lst1= []
    lst2 = []

    for obj in lst:
        if condition(obj):
            lst1.append(obj)
        else:
            lst2.append(obj)
    return lst1, lst2


def children_and_adults(people):
    return partition(people, lambda person: person.age < 18)