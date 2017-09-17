from sys import stdin

def allSub(lst):
    s = tuple(lst)
    for size in range(1, len(s) + 1):
        for index in range(len(s) + 1 - size):
            yield lst[index:index + size]
            
def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

graph, edges = {}, []

edge = stdin.readline().rstrip('\n')
while edge != "**":
    if edge[0] in graph.keys():
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]] = [edge[1]]
        
    if edge[1] in graph.keys():
        graph[edge[1]].append(edge[0])
    else:
        graph[edge[1]] = [edge[0]]

    edges.append(edge)
        
    edge = stdin.readline().rstrip('\n')

all_paths = find_all_paths(graph, 'A', 'B')
path_str = [''.join(x) for x in all_paths]

common = []

for i in range(len(path_str) - 1):
    if i == 0:
        com1 = list(set(list(allSub(path_str[0]))) & set(list(allSub(path_str[1]))))
        for item in com1:
            if len(item) == 2:
                common.append(item)
    else:
        common = list(set(common) & set(list(allSub(path_str[i]))))

for orig in edges:
    for com in common:
        if com == orig[::-1]:
            common.remove(com)
            common.append(orig)
            
if len(all_paths) == 1:
    for i in range(len(all_paths[0]) - 1):
        common.append(all_paths[0][i] + all_paths[0][i + 1])

for i in common:
    print i

print 'There are', len(common), 'disconnecting roads.'
