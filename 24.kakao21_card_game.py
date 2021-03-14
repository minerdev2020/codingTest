# 해설 참조한 풀이
from collections import deque
from itertools import permutations
from copy import deepcopy

dp = {}

def bfs(s, e, board, hash_code):
    if hash_code not in dp:
        dp[hash_code] = {}
    
    start = tuple(s[0])
    end = tuple(e[0])
    if start in dp[hash_code] and end in dp[hash_code][start]:
        return dp[hash_code][start][end]
    
    queue = deque()
    queue.append(s)
    count = len(queue)
    step = 0
    while queue:
        cursor = queue.popleft()
        if cursor == e:
            if start not in dp[hash_code]:
                dp[hash_code][start] = {}
                
            dp[hash_code][start][end] = step
            return step
        
        if cursor[0][0] + 1 < 4:
            queue.append([[cursor[0][0] + 1, cursor[0][1]], board[cursor[0][0] + 1][cursor[0][1]]])
        if cursor[0][1] + 1 < 4:
            queue.append([[cursor[0][0], cursor[0][1] + 1], board[cursor[0][0]][cursor[0][1] + 1]])
        if cursor[0][0] - 1 >= 0:
            queue.append([[cursor[0][0] - 1, cursor[0][1]], board[cursor[0][0] - 1][cursor[0][1]]])
        if cursor[0][1] - 1 >= 0:
            queue.append([[cursor[0][0], cursor[0][1] - 1], board[cursor[0][0]][cursor[0][1] - 1]])
        
        for i in range(cursor[0][0] + 1, 4):
            if board[i][cursor[0][1]] > 0:
                queue.append([[i, cursor[0][1]], board[i][cursor[0][1]]])
                break
            
            elif i == 3:
                queue.append([[i, cursor[0][1]], board[i][cursor[0][1]]])
                
        for i in range(cursor[0][0] - 1, -1, -1):
            if board[i][cursor[0][1]] > 0:
                queue.append([[i, cursor[0][1]], board[i][cursor[0][1]]])
                break
            
            elif i == 0:
                queue.append([[i, cursor[0][1]], board[i][cursor[0][1]]])
                
        for i in range(cursor[0][1] + 1, 4):
            if board[cursor[0][0]][i] > 0:
                queue.append([[cursor[0][0], i], board[cursor[0][0]][i]])
                break
            
            elif i == 3:
                queue.append([[cursor[0][0], i], board[cursor[0][0]][i]])
                
        for i in range(cursor[0][1] - 1, -1, -1):
            if board[cursor[0][0]][i] > 0:
                queue.append([[cursor[0][0], i], board[cursor[0][0]][i]])
                break
            
            elif i == 0:
                queue.append([[cursor[0][0], i], board[cursor[0][0]][i]])
                                
        count -= 1
        if count == 0:
            count = len(queue)
            step += 1
        
    return -1

def dfs(card_pos, board, permutation, total_count, c, start):
    if not permutation:
        total_count.append(c)
        return
    
    card = permutation.pop(0)

    new_board = deepcopy(board)
    new_board[card_pos[card][0][0]][card_pos[card][0][1]] = 0
    new_board[card_pos[card][1][0]][card_pos[card][1][1]] = 0
    hash_code = hash(tuple(map(tuple, board)))
    
    c1 = c + bfs(start, [card_pos[card][0], card], board, hash_code) + bfs([card_pos[card][0], card], [card_pos[card][1], card], board, hash_code)
    dfs(card_pos, new_board, permutation.copy(), total_count, c1, [card_pos[card][1], card])
    
    c2 = c + bfs(start, [card_pos[card][1], card], board, hash_code) + bfs([card_pos[card][1], card], [card_pos[card][0], card], board, hash_code)
    dfs(card_pos, new_board, permutation.copy(), total_count, c2, [card_pos[card][0], card])

def solution(board, r, c):
    dp.clear()
    
    temp = set()
    for b in board:
        temp.update(b)
    n = len(temp) - 1
    
    card_pos = {}
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col > 0:
                if col not in card_pos:
                    card_pos[col] = []
                    
                card_pos[col].append([y, x])
                    
    steps = []
    permutations_list = list(permutations([i for i in range(1, n + 1)]))
    for permutation in permutations_list:
        total_count = []
        dfs(card_pos, board, list(permutation), total_count, 0, [[r, c], board[r][c]])
        steps.append(min(total_count))
            
    return min(steps) + n * 2

# 다른 사람의 풀이
def ctrl(board, x0, y0, dx, dy):
    for i in range(1, 4):
        if 0 <= (x1 := x0 + dx * i) < 4 and 0 <= (y1 := y0 + dy * i) < 4:
            if board[x1][y1] > 0:
                return (x1, y1)
            l = i
    return (x0 + dx * l, y0 + dy * l)

def move(board, xy0, xy1):
    dist = [[6] * 4 for _ in range(4)]
    q = deque([(xy0, 0)])
    while q:
        [x, y], d = q.popleft()
        if d < dist[x][y]:
            dist[x][y] = d
            for dx, dy in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
                if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                    q.append(((x + dx, y + dy), d + 1))
                    q.append((ctrl(board, x, y, dx, dy), d + 1))
    return dist[xy1[0]][xy1[1]]

def solution1(board, r, c):
    loc = {k: [] for k in range(1, 7)}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                loc[board[i][j]].append((i, j))
    minv = 100
    for p in permutations(filter(lambda v: v, loc.values())):
        sumv = 0
        xys = [(r, c)]
        stage = [[v for v in w] for w in board]
        for xy1, xy2 in p:
            vs = [(move(stage, xy, xy1) + move(stage, xy1, xy2), xy2) for xy in xys]\
               + [(move(stage, xy, xy2) + move(stage, xy2, xy1), xy1) for xy in xys]
            stage[xy1[0]][xy1[1]] = stage[xy2[0]][xy2[1]] = 0
            sumv += 2 + (mvn := min(vs)[0])
            xys = [xy for m, xy in vs if m == mvn]
        minv = min(sumv, minv)
    return minv

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
print(solution([[3,4,0,2],[5,0,1,4],[0,1,6,5],[2,0,6,3]], 0, 1))