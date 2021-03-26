def check(braket):    
    stack = []
    stack.append(braket[0])
    for b in braket[1:]:
        if stack and stack[-1] == '(' and b == ')':
            stack.pop()    
        else:
            stack.append(b)
            
    return len(stack) == 0

def solution(p):
    if not p:
        return p
    
    u = ''
    v = ''
        
    count1 = 0
    count2 = 0
    for i in range(len(p)):
        u += p[i]
        if p[i] == '(':
            count1 += 1
        else:
            count2 += 1      
        if count1 == count2:
            v = p[i + 1:]
            break

    answer = ''
    if check(u):
        answer += u + solution(v)
    else:
        u = ''.join(list(map(lambda x: '(' if x == ')' else ')', u[1:-1])))
        answer += '(' + solution(v) + ')' + u
    
    return answer
    
print(solution('(()())()')) # '(()())()'
print(solution(')('))       # '()'          
print(solution('()))((()')) # '()(())()'