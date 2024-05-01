def solution(num_list):
    odd_list = [num for num in num_list if num % 2 != 0]
    return [len(num_list)-len(odd_list), len(odd_list)]