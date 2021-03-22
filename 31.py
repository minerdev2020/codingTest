import sys
input = sys.stdin.readline

def solution(m, n, nums):
    i, j = 0, n-1
    flag = True
    while i < j:
        if nums[i] + nums[j] ==  m:
            print('yes %d %d' %(nums[i], nums[j]))
            flag = False
            break
        elif nums[i] + nums[j] < m:
            i += 1
        else:
            j -= 1
    if flag:
        print("danger")
    return

while True:
    try:
        nums = []
        m = int(input()) * 10000000
        n = int(input())
        for i in range(n):
            nums.append(int(input()))
        nums.sort()
        solution(m, n, nums)
    except:
        break
