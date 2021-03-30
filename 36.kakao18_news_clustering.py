# 내 풀이
def solution(str1, str2):    
    str1_temp = str1.lower()
    str1_set = []
    for i in range(len(str1) - 1):
        if str1_temp[i:i+2].isalpha():
            str1_set.append(str1_temp[i:i+2])
            
    str2_temp = str2.lower()
    str2_set = []
    for i in range(len(str2) - 1):
        if str2_temp[i:i+2].isalpha():
            str2_set.append(str2_temp[i:i+2])
    
    if not str1_set and not str2_set:
        return 1 * 65536
    
    sum_len = 0
    intersection_len = 0
    sum_set = set(str1_set)
    sum_set.update(str2_set)
    sum_set = list(sum_set)
    for e in sum_set:
        count1 = str1_set.count(e)
        count2 = str2_set.count(e)            
        sum_len += max(count1, count2)
        if count2:
            intersection_len += min(count1, count2)
        
    return int(intersection_len / sum_len * 65536)

print(solution('FRANCE', 'french')) # 16384
print(solution('handshake', 'shake hands')) # 65536
print(solution('aa1+aa2', 'AAAA12')) # 43690
print(solution('E=M*C^2', 'e=m*c^2')) # 65536

# 다른 사람의 풀이
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)