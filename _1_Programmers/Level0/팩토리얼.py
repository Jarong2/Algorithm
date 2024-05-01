import math


def solution(n):
    answer = 0
    factorials = [math.factorial(num) for num in range(1, 11)]
    for idx, f in enumerate(factorials):
        if f <= n:
            answer = idx+1
    return answer