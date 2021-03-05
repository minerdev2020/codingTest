# 내 풀이
def solution(citations):
    answer = -1
    citations.sort()

    for h in range(len(citations) + 1):
        up_count = 0
        down_count = 0
        for ct in citations:
            if h <= ct:
                up_count += 1

            else:
                down_count += 1
    
        print(citations, h, up_count, down_count)
        if h <= up_count and h >= down_count and answer < h:
            answer = h

    return answer

# 다른 사람의 풀이 1
def solution1(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i

    return 0

# 다른 사람의 풀이 2
def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([3, 3, 3]))

print(solution1([3, 0, 6, 1, 5]))
print(solution2([3, 0, 6, 1, 5]))