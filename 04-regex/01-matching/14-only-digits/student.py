# Write your code here
import re

def only_digits(string):
    return bool(re.fullmatch(r"\d*", string))