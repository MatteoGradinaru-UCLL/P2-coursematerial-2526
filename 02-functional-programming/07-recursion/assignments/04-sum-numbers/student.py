def sum_numbers(number):
    text = str(number).replace("-", "")

    if len(text) <= 1:
        return int(text)
    
    return int(text[0]) + sum_numbers(int(text[1:]))