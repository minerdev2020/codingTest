def solution(s):
    if(len(s) == 1):
        return 1
    answer = 0
    for i in range(1, len(s) // 2 + 1):
        tp_str = s[:i]
        cnt = 0
        tp_ans = 0
        for j in range(i, len(s), i):
            if tp_str == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 0:
                    tp_ans += i
                else:
                    tp_ans += (i + len(str(cnt + 1)))
                cnt = 0
                tp_str = s[j:j + i]

        if cnt == 0:
            tp_ans += len(tp_str)
        else:
            tp_ans += (i + len(str(cnt + 1)))

        if answer == 0:
            answer = tp_ans
        else:
            answer = min(answer, tp_ans)
    return answer
