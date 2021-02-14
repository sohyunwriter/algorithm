import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def cnt_cycle(graph, n):
    parent = [i for i in range(0, n+1)]
    cycle_cnt = 0

    for a, b in enumerate(graph):
        if a == 0:
            continue
        if find_parent(parent, a) == find_parent(parent, b):
            cycle_cnt += 1
        else:
            union_parent(parent, a, b)
    #print(parent)
    return cycle_cnt

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = [0] + list(map(int, input().split()))
        answer = cnt_cycle(graph, N)
        print(answer)
