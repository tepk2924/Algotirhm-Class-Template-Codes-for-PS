def Make_Sparse_Table(parent:dict):
    sparse_table = [parent]
    while True:
        last_row = sparse_table[-1]
        new_row = {}
        continuing = False
        for key in parent:
            a = last_row[key]
            if a is None: continue
            b = last_row[a]
            if b is None: continue
            new_row[key] = b
            continuing = True
        if not continuing: break
        sparse_table.append(new_row)
    return sparse_table