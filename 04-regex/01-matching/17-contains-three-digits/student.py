# Write your code here
import re

def contains_three_digits(string):
    return bool(re.search(r"\d.*\d.*\d", string))