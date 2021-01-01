def solution(S, P, Q):
    dnadict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    mydict = {'A':[0], 'C':[0], 'G':[0]}
    ans = []

    for i in S:
        for j in mydict.keys():
            mydict[j].append(mydict[j][-1])

        if i != 'T':
            mydict[i][-1] += 1

    for i in range(len(P)):
        if Q[i] == P[i]:
            ans.append(dnadict[S[Q[i]]])
        elif mydict['A'][Q[i]+1] - mydict['A'][P[i]] > 0:
            ans.append(dnadict['A'])
        elif mydict['C'][Q[i]+1] - mydict['C'][P[i]] > 0:
            ans.append(dnadict['C'])
        elif mydict['G'][Q[i]+1] - mydict['G'][P[i]] > 0:
            ans.append(dnadict['G'])
        else:
            ans.append(dnadict['T'])
    
    return ans
