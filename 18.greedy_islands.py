# 내 풀이 (프림)
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[0])
    connected = [costs[0][0]]
    edges = []
    for e in costs:
        if e[0] == connected[0]:
            edges.append(e)
        
        elif e[1] == connected[0]:
            edges.append(e)
    
    while edges:
        edges.sort(key=lambda x: x[2], reverse=True)
        print(edges)
        edge = edges.pop()
        if edge[0] not in connected:
            answer += edge[2]
            connected.append(edge[0])
            for e in costs:
                if e[0] == edge[0]:
                    edges.append(e)
                    
                elif e[1] == edge[0]:
                    edges.append(e)

        elif edge[1] not in connected:
            answer += edge[2]
            connected.append(edge[1])
            for e in costs:
                if e[1] == edge[1]:
                    edges.append(e)
                    
                elif e[0] == edge[1]:
                    edges.append(e)
                    
    return answer

# 다른 사람의 풀이 (크루스칼)
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer

print(solution(4, [[0, 1, 7], [0, 3, 5], [1, 2, 8], [1, 3, 9], [2, 4, 5],
                   [3, 4, 7], [3, 5, 6], [4, 5, 8], [4, 6, 9], [5, 6, 11]]))