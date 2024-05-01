# 01, 반복문
def solution(my_string, n):
    new_string = ''
    for string in my_string:
        new_string += string*n
    return new_string


# 02. list comprehension, join
def solution(my_string, n):
    return ''.join([string*n for string in my_string]) # list 안 씌워도 됨
