# 내 풀이
def solution(routes):
    routes.sort()
    answer= []
    common = routes[0]
    for route in routes[1:]:
        if route[1] <= common[1] and route[0] >= common[0]:
            common[0] = route[0]
            common[1] = route[1]
            
        elif route[0] <= common[1] and route[0] >= common[0]:
            common[0] = route[0]
            
        elif route[1] <= common[1] and route[1] >= common[0]:
            common[1] = route[1]
                       
        elif route[1] >= common[1] and route[0] <= common[0]:
            pass
        
        else:
            answer.append(common)
            common = route
            
    answer.append(common)                
    return len(answer)

# 다른 사람의 풀이1
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

# 다른 사람의 풀이2
import heapq

def solution(routes):
    routes.sort(key=lambda x:x[0])

    answer = 0
    h = [30001]
    for r in routes:
        earliestend = heapq.heappop(h)
        if r[0] > earliestend:
            answer += 1
            h.clear()
        else:
            heapq.heappush(h, earliestend)
        heapq.heappush(h, r[1])
    else:
        if len(h) != 0:
            answer += 1
    return answer

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])) #2
print(solution([[-2, -1], [1, 2], [-3, 0]])) #2
print(solution([[0, 0]])) #1
print(solution([[0, 1], [0, 1], [1, 2]])) #1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]])) #4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])) #2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]])) #2