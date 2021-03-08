# 내 풀이
from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:                
        result = {}
        for order in orders:
            order_split = list(order)
            order_split.sort()
            combi_list = list(combinations(order_split, c))
            for combi in combi_list:
                if combi not in result:
                    result[combi] = 0
                    
                result[combi] += 1
  
        if result:      
            temp = sorted(result.items(), key=lambda item: item[1], reverse=True)
            if temp[0][1] > 1:
                for t in temp:
                    if t[1] == temp[0][1]:
                        answer.append(''.join(t[0]))
                        
                    else:
                        break

    answer.sort()
    return answer

# 다른 사람의 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))