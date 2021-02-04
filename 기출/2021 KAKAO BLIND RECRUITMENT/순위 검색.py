from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

# 각 info에 대한 16가지 조합 만들기
def combi_info(info_key):
    result = []
    for num in range(5):
        for part_key in combinations(info_key, num):
            result.append(''.join(part_key))
    return result

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    # info 처리
    for pinfo in info:
        pinfo = pinfo.split()
        pinfo_key = pinfo[:-1]
        pinfo_score = int(pinfo[-1])
        for part_key in combi_info(pinfo_key):  # query의 key로 나올 수 있는 combination
            info_dict[part_key].append(pinfo_score)

    # 각 key의 value들 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    # query 처리
    for q in query:
        q = q.split()
        q_key = ''
        q_score = int(q[-1])
        for i in q[:-1]:
            if i != 'and' and i != '-':
                q_key += i

        result = info_dict[q_key]
        answer.append(len(result) - bisect_left(result, q_score))   # lower bound
    return answer


#info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
#query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
#print(solution(info, query))
