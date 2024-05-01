def solution(price):
    sale_percent = 0.05 if price >= 100000 else 0 # 기본 할인율
    if price >= 500000:
        sale_percent = 0.2
    elif price >= 300000:
        sale_percent = 0.1
    return price * (1 - sale_percent) // 1 # int로 소수점 버려도 됨