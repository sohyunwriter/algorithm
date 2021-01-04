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

def is_cycle(edges, v, e):
    parent = [i for i in range(0, v+1)]
    cycle = False
    #print(parent)

    for a, b in edges:
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        else:
            union_parent(parent, a, b)

    return cycle

### test ###
v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
#print(v, e, edges)
print(is_cycle(edges, v, e))
