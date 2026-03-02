def group_by(xs, key_function):
    result = {}
    for obj in xs:
        key = key_function(obj)
        if key not in result:
            result[key] = []
        result[key].append(obj)
    return result
