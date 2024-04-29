def solution(array):
    # 숫자별 빈도 수
    freq_dict = {n: array.count(n) for n in set(array)}
    count_list = sorted(list(freq_dict.values()))

    # 최빈값이 여러개인 경우
    if (len(count_list) > 1) and (count_list[-1] == count_list[-2]):
        return -1
    else:
        rev_freq_dict = {v: k for k, v in freq_dict.items()}
        return rev_freq_dict[count_list[-1]]