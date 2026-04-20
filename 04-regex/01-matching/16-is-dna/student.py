# Write your code here
import re

def is_dna(string):
    return bool(re.search(r"(G|A|T|C)+", string))
