# Write your code here
import re

def one_or_more_b(string):
    return bool(re.fullmatch(r"b+", string))