from collections import Counter

def makeset(str1):
    str_set = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            temp = (str1[i] + str1[i+1])
            str_set.append((str1[i] + str1[i+1]))
    return str_set

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    elements1 = makeset(str1)
    elements2 = makeset(str2)
    if len(elements1) == len(elements2) == 0:
        return 1 * 65536

    ele1_c = Counter(elements1)
    ele2_c = Counter(elements2)
    intersect = set(elements1) & set(elements2)
    union = set(elements1) | set(elements2)
    intersect = sum([min(ele1_c[i], ele2_c[i]) for i in intersect])
    union = sum([max(ele1_c[i], ele2_c[i]) for i in union])
    return int((intersect/union) * 65536)
