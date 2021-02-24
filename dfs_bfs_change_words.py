answer = []

def one_letter_diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            
        if count > 1:
            return False
        
    if count == 1:
        return True
    
    else:
        return False
        
# 제출한 풀이
def dfs(current : str, words : list, target : str, route : list):
    if current == target:
        global answer_list
        answer.append(route)
        return
    
    for word in words:
        if word not in route and one_letter_diff(current, word):
            new_route = route.copy()
            new_route.append(word)
            dfs(word, words, target, new_route)

# 더 좋은 풀이
def bfs(current : str, words : list, target : str):
    if current == target:
        return 0
    
    queue = []
    queue.append(current)
    count = 0
    width = len(queue)
    while(queue):
        if width == 0:
            width = len(queue)
            count += 1
            
        word = queue.pop(0)
        width -= 1
        
        if (word == target):
            return count
        
        for w in words:
            if one_letter_diff(word, w):
                queue.append(w)
        
    return 0
                
def solution(begin, target, words):
    if target not in words:
        return 0
        
    dfs(begin, words, target, [])   
        
    return len(min(answer))

def solution1(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, words, target)   

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))

print(solution1('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution1('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))