def solution(brown, yellow):
    answer = []

    num = brown + yellow
    for x in range(num, 1, -1):
        if num % x == 0:
            y = num // x

            if x < y: 
                break

            elif brown == (x + y) * 2 - 4:
                answer.append(x)
                answer.append(y)

    return answer

print(solution(8, 1))