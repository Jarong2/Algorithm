import re

def solution(my_string):
    string = re.sub('[a-z]', '', my_string)
    return sorted([int(s) for s in string])