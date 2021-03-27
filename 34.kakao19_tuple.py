import re

def solution(s):
    answer = []
    
    s = s[1:-1]
    elements = re.findall('{[0-9,]+}', s)
    elements.sort(key=lambda x: x.count(','))
    for e in elements:
        temp = e[1:-1].split(',')
        for t in temp:
            if t not in answer:
                answer.append(t)
                        
    return list(map(int, answer))

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))    # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))    # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))                 # [111, 20]
print(solution("{{123}}"))                          # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))    # [3, 2, 4, 1]