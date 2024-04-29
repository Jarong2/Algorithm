# 01. list comprehension
def solution(numbers):
    return [n*2 for n in numbers]


# 02. map
def solution(numbers):
    return list(map(lambda x: x*2, numbers))