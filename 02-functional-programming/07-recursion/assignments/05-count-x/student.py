# def countX(text):
#     if len(text) < 1:
#         return 0
    
#     if text[0] == "x":
#         return 1 + countX(text[1:])
#     else:
#         return 0 + countX(text[1:])
    


def countX(text):
    if len(text) < 1:
        return 0
    
    if text[0] == "x":
        return 1 + countX(text[1:])
    else:
        return 0 + countX(text[1:])