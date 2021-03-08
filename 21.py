from itertools import combinations

def solution(orders, course):
    result = []
    temp = dict()
    for n in course:
        temp[n] = []
        
    for order in orders:
        for n in course:
            if n <= len(order):
                temp[n] += (list(combinations(sorted(order),n)))

    for menus in temp.values():
        max_num = 2
        for menu in menus:
            cnt = menus.count(menu)
            if cnt > max_num:
                max_num = cnt

        for menu in menus:
            rst = ''.join(menu)
            if max_num == menus.count(menu) and rst not in result:
                result.append(rst)

    return sorted(result)
