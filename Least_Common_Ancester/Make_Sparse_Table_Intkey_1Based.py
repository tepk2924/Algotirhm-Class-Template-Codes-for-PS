def Make_Sparse_Table(parent:list):
    '''
    parent[i] means parent of node i, where all nodes are indexed by numbers from 1 to N.
    parent[0] is not used.
    '''
    sparse_table = [parent]
    N = len(parent) - 1
    while True:
        last_row = sparse_table[-1]
        new_row = [None]*-~N
        continuing = False
        for idx in range(1, N + 1):
            a = last_row[idx]
            if a is None: continue
            b = last_row[a]
            if b is None: continue
            new_row[idx] = b
            continuing = True
        if not continuing: break
        sparse_table.append(new_row)
    return sparse_table