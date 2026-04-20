# Write your code here
import re

def one_or_more_a(string):
    return bool(re.fullmatch(r"a+", string))