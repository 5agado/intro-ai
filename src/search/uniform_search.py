def dfs(graph, start, end, path = []):
    print(start)
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            respath = dfs(graph, node, end, path)
            if respath: 
                return respath
    return None

def bfs(graph, start, end, path = []):
    stack = list()
    explored = list()
    path = {}
    stack.append(start)
    while len(stack) > 0:
        current = stack.pop(0)
        explored.append(current)
        for node in graph[current]:
            if node not in explored:
                path[node] = current
                if node == end:
                    print(explored)
                    respath = [node]
                    while True:
                        respath.insert(0, path[node])
                        node = path[node]
                        if node == start:
                            return respath  
                stack.append(node)
            
    return None

#for a* g+h need to be used
#instead of only g (h = cost to the goal)
def ucs(graph, start, end):
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
    
graph = {'A': ['B', 'C', 'D'],
              'B': ['E', 'F'],
              'C': [],
              'D': ['G', 'H'],
              'E': ['I', 'L'],
              'F': [],
              'G': ['M', 'N'],
              'H': [],
              'I': [],
              'L': [],
              'M': [],
              'N': [],
              }

romaniaGraph = {'Sibiu': [('Vilcea', 80), ('Fagaras', 90)],
              'Vilcea': [('Pitesti', 97)],
              'Fagaras': [('Bucharest', 11)],
              'Pitesti': [('Bucharest', 101)],
              }

#print(bfs(graph, 'A', 'N'))
#print(ucs(romaniaGraph, 'Sibiu', 'Bucharest'))