# 01. if문 사용
def solution(n):
    return sum(num for num in range(1, n+1) if num % 2 == 0)


# 02. range step 활용
def solution(n):
    return sum(range(2, n+1, 2))
