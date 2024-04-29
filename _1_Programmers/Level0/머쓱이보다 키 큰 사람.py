# 01. list comprehension
def solution(array, height):
    return len([h for h in array if h > height])


# 02. sort, index
def solution(array, height):
    array.append(height)
    sorted_array = sorted(array, reverse=True)
    return sorted_array.index(height)