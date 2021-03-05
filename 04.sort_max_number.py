from functools import cmp_to_key

# 내 풀이
# a가 b보다 작을때 1이 나오는 함수
def lesser(a : str, b : str):
    if len(a) == len(b):
        return (a < b) - (a > b)

    else:
        max_num = a
        min_num = b
        sign = 1
        if len(a) < len(b):
            max_num, min_num = min_num, max_num
            sign = -1

        i = 0
        length = len(min_num)
        while(i < len(max_num)):
            if max_num[i:].startswith(min_num):
                c = max_num[length + i:]
                if not c.startswith(min_num):
                    if min_num.startswith(c):
                        return sign * ((c < min_num[len(c):]) - (c > min_num[len(c):]))
                    
                    else:
                        return sign * ((c < min_num) - (c > min_num))

            else:
                break

            i += length

        return (a < b) - (a > b)

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    print(numbers)
    print(sorted(numbers, reverse=True))
    numbers.sort(key=cmp_to_key(lesser))
    print(numbers)

    is_all_zero = True
    for number in numbers:
        answer += number
        if number != '0':
            is_all_zero = False

    if is_all_zero:
        answer = '0'

    return answer

# 다른 사람의 풀이 1
def solution1(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # join함수는 문자열을 합치는 함수, 또한 여기서 '000...'을 걸러낸다
    return str(int(''.join(numbers))) 

# 다른 사람의 풀이 2
# 가능한 경우를 실제로 숫자로 만들어 봐서 비교하는 함수
def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

def solution2(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([214, 21421]))
print(solution([21, 21212]))
print(solution([21, 21211]))
print(solution([21, 21214]))