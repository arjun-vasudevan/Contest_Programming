from sys import stdin

def find_path(graph, start, end, path = []):
    path = path + [start]
    
    if start == end:
        return path

    if not graph.has_key(start):
        return None
        
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

N, M, A, B = [int(_) for _ in stdin.readline().rstrip('\n').split()]
graph = {}

for i in range(M):
    roads = [int(_) for _ in stdin.readline().rstrip('\n').split()]
    if roads[0] in graph:
        graph[roads[0]].append(roads[1])
    else:
        graph[roads[0]] = [roads[1]]

    if roads[1] in graph:
        graph[roads[1]].append(roads[0])
    else:
        graph[roads[1]] = [roads[0]]

print "NO SHAHIR!" if not find_path(graph, A, B) else "GO SHAHIR!"
