def take_while(xs, condition):
    true_list = []
    false_list = []
    found_false = False

    for element in xs:
        if not found_false and condition(element):
            true_list.append(element)
        else:
            found_false = True
            false_list.append(element)
    return true_list, false_list