# 내 풀이
def solution(s):
    answer = 1001
    length = len(s)
    
    if length == 1:
        return 1
    
    for i in range(1, length):
        result = ''
        current_idx = 0
        count = 0
        token = ''
        while current_idx < length:
            if token and token != s[current_idx:current_idx + i]:
                result += f'{count}{token}' if count > 1 else token
                count = 0
                
            token = s[current_idx:current_idx + i]
            count += 1
            
            current_idx += i
    
        if token and token != s[current_idx:current_idx + i]:
            result += f'{count}{token}' if count > 1 else token
                 
        print(result)
                    
        if answer > len(result):
            answer = len(result)
        
    return answer

# 다른 사람의 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution1(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

print(solution("aabbaccc"))                 # 7
print(solution("ababcdcdababcdcd"))         # 9
print(solution("abcabcdede"))               # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd"))        # 17
print(solution("a"))                        # 1
print(solution("aa"))                       # 2
print(solution("ab"))                       # 2