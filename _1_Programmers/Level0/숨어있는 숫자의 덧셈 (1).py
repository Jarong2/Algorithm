import re


def solution(my_string):
    string = re.sub('[a-zA-Z]', '', my_string)
    return sum([int(s) for s in string])