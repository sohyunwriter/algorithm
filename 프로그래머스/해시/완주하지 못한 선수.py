from collections import defaultdict

def solution(participant, completion):
    answer = ''
    mydict = defaultdict(int)
    
    for i in completion:
        mydict[i] += 1
    
    for i in participant:
        if not mydict[i]:
            answer = i
            break
        mydict[i] -= 1
        
    return answer
