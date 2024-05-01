def solution(n, k): # n: 양꼬치, k: 음료수
    return n * 12000 + (k - n//10) * 2000 # 11800n + 2000k