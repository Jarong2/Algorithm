def solution(array):
    # 값이 1개인 경우도 고려해야 한다.
    median_idx = int(len(array)/2) if len(array) > 1 else 0
    sorted_array = sorted(array)
    return sorted_array[median_idx]