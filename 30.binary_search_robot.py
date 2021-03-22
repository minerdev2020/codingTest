# 다른 사람의 답안 참고함
import sys
input = sys.stdin.readline # 더 빠르고 정확한 유저 입력 함수

def solution(target, n, lego_list):
    if not lego_list:
        return 'danger'
    
    lego_list.sort()
    left = 0
    right = n - 1
    while(left < right):
        result = lego_list[left] + lego_list[right]
        if result < target:           
            left += 1
        elif result > target:
            right -= 1
        else:
            # return 'yes {0} {1}'.format(lego_list[left], lego_list[right])
            # return 'yes %d %d' % (lego_list[left], lego_list[right])
            return f'yes {lego_list[left]} {lego_list[right]}'
            
    return 'danger'

print(solution(1 * 10000000, 4, [9999998, 1, 2, 9999999]))  # yes 1 9999999
print(solution(3 * 10000000, 4, [9999998, 1, 2, 9999999]))  # danger

# # 입력이 없으면 끝남
# while True:
#     try:
#         x = int(input()) * 10000000
#         n = int(input())
#         lego_list = [int(input()) for _ in range(n)]
#         print(solution(x, n, lego_list))
        
#     except:
#         break