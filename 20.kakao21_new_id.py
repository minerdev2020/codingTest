import re

# 내 풀이
def solution(new_id: str):
    print(0, new_id)
    print(1, new_id.lower())
    
    # 1, 2단계
    answer = re.sub('[^a-z0-9_.\-]', '', new_id.lower())
    print(2, answer)

    # 3단계
    answer = re.sub('\.\.+', '.', answer)
    print(3, answer)
    
    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
        
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    print(4, answer)
    
    # 5단계
    if not answer:
        answer = 'a'
        
    print(5, answer)
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
            
    print(6, answer)
    
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer

# 다른 사람의 풀이
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))