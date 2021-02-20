def prime_num(num):
    if num <= 1:
        return False
    
    i = 2
    n = num ** 0.5
    while i <= n:
        if num % i == 0:
            return False
        
        i += 1
        
    return True

def comb(num, numbers, result):
    if num != '' and int(num) not in result:
        result.append(int(num))
        
    if numbers == '':
        return
    
    for n in numbers:
        temp = numbers.replace(n, '', 1)
        comb(num + n, temp, result)

def solution(numbers):
    answer = 0
    
    result = []
    comb('', numbers, result)
    
    for n in result:
        if prime_num(n):
            answer += 1
    
    return answer

print(solution("17"))