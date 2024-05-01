def solution(emergency):
    sort_emergency = sorted(emergency, reverse=True)
    return [sort_emergency.index(e)+1 for e in emergency]