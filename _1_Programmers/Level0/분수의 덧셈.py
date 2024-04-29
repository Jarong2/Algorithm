# 최대공약수 : 약분
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수 : 공통분모
def lcm(a, b):
    return a * b / gcd(a, b)


def solution(numer1, denom1, numer2, denom2):
    denom = lcm(denom1, denom2) # 공통분모를 구한다.
    numer = (numer1 * denom/denom1) + (numer2 * denom/denom2) # 통분하여 분자를 구한다.
    return [numer/gcd(numer, denom), denom/gcd(numer, denom)] # 최대공약수로 약분하여 기약분수로 나타낸다.