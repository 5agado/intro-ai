#same as UCS, instead that here g+h need to be used
#instead of only g (h = cost to the goal)
def astar(graph, start, end):
    frontier = list()
    costs = {}
    explored = list()
    path = {}
    frontier.append(start)
    costs[start] = 0
    while len(frontier) > 0:
        #take cheapest one. Implement with priority queue
        index = 0
        minv = costs[frontier[index]]
        for i in range(len(frontier)):
            if costs[frontier[i]] < minv:
                minv = costs[frontier[i]]
                index = i
        node = frontier.pop(index)
        if node == end:
            respath = [node]
            while True:
                respath.insert(0, path[node])
                node = path[node]
                if node == start:
                    return respath  
        explored.append(node)
        for child in graph[node]:
            if not child[0] in explored or not child[0] in frontier:
                path[child[0]] = node
                frontier.append(child[0])
                costs[child[0]] = costs[node] + child[1]
            elif costs[child[0]] > (costs[node] + child[1]):
                path[child[0]] = node
                costs[child[0]] = costs[node] + child[1]
            
            
    return None