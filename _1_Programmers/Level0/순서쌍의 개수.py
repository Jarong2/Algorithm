# 01. list comprehension
def solution(n):
    return len([i for i in range(1, n+1) if n % i==0])


# 02. 반복 수 줄이기
def solution(n):
    pair = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n ** 0.5 == i:
                pair += 1
            else:
                pair += 2
    return pair