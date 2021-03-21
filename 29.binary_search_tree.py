def compare(tree_list, target, mid):
    tree_sum = 0
    for height in tree_list:
        if height - mid > 0:
            tree_sum += height - mid
        
    return tree_sum >= target

def solution(target, tree_list):
    left = 0
    right = sum(tree_list)
    while(left + 1 < right):
        mid = (left + right) // 2
        result = compare(tree_list, target, mid)
        print(left, mid, right, result)
        if result:           
            left = mid
        else:
            right = mid
            
    return left

print(solution(7, [20, 15, 10, 17]))  # 15
print(solution(4, [20, 15, 10, 17]))  # 16
print(solution(62, [20, 15, 10, 17])) # 0

# N, M = map(int, input().split())
# tree_list = list(map(int, input().split()))
# print(solution(M, tree_list))