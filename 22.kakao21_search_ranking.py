# 내 풀이
import bisect

def make_tree(keys, tree):
    if keys:
        for k in keys[0]:
            if len(keys) == 1:
                tree[k] = []
            else:
                tree[k] = {}
            make_tree(keys[1:], tree[k])    

def solution(info, query):
    keys = [['cpp', 'java', 'python', '-'], ['backend', 'frontend', '-'], ['junior', 'senior', '-'], ['chicken', 'pizza', '-']]
    tree = {}
    make_tree(keys, tree)
    person_infos = [i.split() for i in info]
    person_infos.sort(key=lambda x: int(x[4]))
    for person_info in person_infos:
        temp = int(person_info[4])
        tree[person_info[0]][person_info[1]][person_info[2]][person_info[3]].append(temp)
        
        tree['-'][person_info[1]][person_info[2]][person_info[3]].append(temp)
        tree[person_info[0]]['-'][person_info[2]][person_info[3]].append(temp)
        tree[person_info[0]][person_info[1]]['-'][person_info[3]].append(temp)
        tree[person_info[0]][person_info[1]][person_info[2]]['-'].append(temp)
        
        tree['-']['-'][person_info[2]][person_info[3]].append(temp)
        tree['-'][person_info[1]]['-'][person_info[3]].append(temp)
        tree['-'][person_info[1]][person_info[2]]['-'].append(temp)
        
        tree[person_info[0]]['-']['-'][person_info[3]].append(temp)
        tree[person_info[0]]['-'][person_info[2]]['-'].append(temp)

        tree[person_info[0]][person_info[1]]['-']['-'].append(temp)

        tree['-']['-']['-'][person_info[3]].append(temp)
        tree['-']['-'][person_info[2]]['-'].append(temp)
        tree['-'][person_info[1]]['-']['-'].append(temp)
        tree[person_info[0]]['-']['-']['-'].append(temp)

        
        tree['-']['-']['-']['-'].append(temp)
        
    answer = [0 for i in range(len(query))]
    for q_idx, q in enumerate(query):
        temp = q.split(' and ')
        last = temp.pop()
        temp += last.split()     
        temp[4] = int(temp[4])
        scores = tree[temp[0]][temp[1]][temp[2]][temp[3]]
        if scores:
            answer[q_idx] += len(scores) - bisect.bisect_left(scores, temp[4])
                
    return answer

# 다른 사람의 풀이 1
from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left

def solution1(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]

# 다른 사람의 풀이 2
def solution2(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer

print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))