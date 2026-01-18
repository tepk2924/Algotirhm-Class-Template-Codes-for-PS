def Trace_Upward(sparse_table, start_point, depth_dist):
    for power, digit in enumerate(f"{depth_dist:b}"[::-1]):
        if digit == '1':
            start_point = sparse_table[power][start_point]
    return start_point

def Lowest_Common_Ancester(sparse_table, depth, u, v):
    '''
    sparse_table[i][k]: dict or list that represents 2**ith ancester of node k in a rooted tree
    (given that 0th ancester of any node is itself, and 1st one is the direct parent.)
    depth[k]: dict or list that contains the depth of node k in a rooted tree
    '''
    if depth[u] > depth[v]:
        depth_diff = depth[u] - depth[v]
        u = Trace_Upward(sparse_table, u, depth_diff)
    elif depth[v] > depth[u]:
        depth_diff = depth[v] - depth[u]
        v = Trace_Upward(sparse_table, v, depth_diff)
    if u == v:
        return u
    for idx in range(len(sparse_table) - 1, -1, -1):
        if sparse_table[idx][u] != sparse_table[idx][v]:
            u = sparse_table[idx][u]
            v = sparse_table[idx][v]
    return sparse_table[0][u]