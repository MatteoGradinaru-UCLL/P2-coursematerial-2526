# Write your code here
import re

def is_valid_student_id(string):
    return bool(re.fullmatch(r"(s|r|S|R)[0-9]{7}", string))