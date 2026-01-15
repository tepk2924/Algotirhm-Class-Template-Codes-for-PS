import sys
import heapq

def Dijkstra_Algorithm(graph, start_pt):
    dists = {key: float('inf') for key in graph}
    mheap = []
    dists[start_pt] = 0
    heapq.heappush(mheap, (0, start_pt))
    visited = set()
    while mheap:
        cost, node = heapq.heappop(mheap)
        if not (node in visited):
            visited.add(node)
            for key, val in graph[node].items():
                if cost + val < dists[key]:
                    dists[key] = cost + val
                    heapq.heappush(mheap, (cost + val, key))
    return dists

V, E = map(int, sys.stdin.readline().split())
start_pt = int(sys.stdin.readline())
graph = {idx:{} for idx in range(1, V + 1)}
'''
key for nodes: any hashable
graph[a][b] == c --> edge from a to b with cost c exists
e.g) graph = {1: {2: 5, 3: 6, "MM": 1}, "MM": {1: 1, 2: 5}, 3: {"MM": 10, 1: 10}}
'''
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

dists = Dijkstra_Algorithm(graph, start_pt)
'''
dists[a] == c --> minimum cost from start_pt to a is c
'''

for nodeidx in range(1, V + 1):
    if dists[nodeidx] == float('inf'):
        sys.stdout.write("INF\n")
    else:
        sys.stdout.write(f"{dists[nodeidx]}\n")