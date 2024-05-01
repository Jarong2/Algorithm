# 01. 내장 함수 사용
def solution(my_string):
    return ''.join(s for s in my_string if s not in 'aeiou')


# 02. re 모듈 활용
import re


def solution(my_string):
    return re.sub('[aeiou]', '', my_string)