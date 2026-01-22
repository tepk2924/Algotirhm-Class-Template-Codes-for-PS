def Knapsack_Problem(items, maxcost):
    '''
    items: [[cost, value], [cost, value], ...]
    maxcost: int
    '''

    max_value_by_cost = [0]*-~maxcost
    #max_value_by_cost[c] means the maximum possible sum of item value within cost c
    #updated upon iterating each item.

    for cost, value in items:
        new_value = max_value_by_cost[:]
        for idx in range(maxcost + 1):
            if idx + cost <= maxcost:
                new_value[idx + cost] = max(max_value_by_cost[idx + cost], max_value_by_cost[idx] + value)
        max_value_by_cost = new_value
    
    return max_value_by_cost[maxcost]