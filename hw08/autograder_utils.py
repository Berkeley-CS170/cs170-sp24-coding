def is_independent_set(adj_list, vertices):
    """
    Return True if vertices is an independent set in adj_list, False otherwise.

    args:
        adj_list:List[List[int]] = the adjacency list of the graph
        vertices:List[int] = a list of vertices

    return:
        bool: True if vertices is an independent set in adj_list, False otherwise.
    """
    for u in vertices:
        for v in vertices:
            if u != v and v in adj_list[u]:
                return False
    return True

def validate_tour(tour, dist_arr):
    """Returns the length of the tour if it is valid, -1 otherwise
    """
    n = len(tour)
    cost = 0
    for i in range(n):
        if dist_arr[tour[i-1]][tour[i]] == float('inf'):
            return -1
        cost += dist_arr[tour[i-1]][tour[i]]
    return cost