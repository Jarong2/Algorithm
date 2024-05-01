def solution(rsp):
    wins = {'0': '5', '2': '0', '5': '2'}
    return ''.join(wins[x] for x in rsp)