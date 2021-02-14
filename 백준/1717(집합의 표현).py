import sys
sys.setrecursionlimit(1000000)  # maximum recursion depth exceed (한도 안 늘리면 runtime error 발생)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

def same_disjoint_set(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    for _ in range(m):
        sig, a, b = map(int, input().split())
        if sig:
            print(same_disjoint_set(parent, a, b))
        else:
            union(parent, a, b)
