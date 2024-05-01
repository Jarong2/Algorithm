import math


def solution(balls, share):
    numer = math.factorial(balls)
    denom = math.factorial(balls-share) * math.factorial(share)
    return numer/denom