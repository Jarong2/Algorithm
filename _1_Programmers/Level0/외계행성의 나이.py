def solution(age):
    new_age = ''
    alpha_age_dict = {str(idx): alpha for idx, alpha in enumerate('abcdefghij')}
    for num in str(age):
        new_age += alpha_age_dict[num]
    return new_age