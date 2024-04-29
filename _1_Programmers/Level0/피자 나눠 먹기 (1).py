# 01. if, else
def solution(n):
    return n // 7 + 1 if n % 7 != 0 else n // 7


# 02. more simple
def solution(n):
    return (n - 1) // 7 + 1