# Write your code here
import re

def contains_a(string):
    return bool(re.search(r"a", string))