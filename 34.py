def right(p):
    cnt = 0
    for s in p:
        if s == '(':
            cnt+=1
        else:
            cnt-=1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False


def divide_uv(p):
    cnt = 0
    check = False
    u = ''
    v = ''
    for s in p:
        if check:
            v += s
        else:
            u += s
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            check = True
    return u, v

def solution(p):
    answer = 0
    if p == '':
        return ''
    u, v = divide_uv(p)

    if right(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        temp_u = u[1:-1]
        for i in temp_u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

