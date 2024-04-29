def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(n):
    # 필요한 최소 피자 수 : 사람 수 * 6 조각 / 최대공약수 / 6 
    return n / gcd(n, 6)