import re
import copy
import itertools

def solution(expression):
    answer = 0
    elements = re.findall('[0-9]+', expression)
    operators = re.findall('[-|+|*]',expression)
    op_check = set(operators)

    expression = []
    for i in range(len(operators)):
        expression.append(elements[i])
        expression.append(operators[i])
    expression.append(elements[-1])
    tp_expression = copy.deepcopy(expression)

    for ops in list(itertools.permutations(op_check)):
        for op in ops:
            tp_ext =  []
            i = 0
            while len(expression) > i:
                if op == expression[i]:
                    temp = 0
                    if op == '+':
                        temp = int(expression[i-1]) + int(expression[i+1])
                    elif op == '-':
                        temp = int(expression[i-1]) - int(expression[i+1])
                    else:
                        temp = int(expression[i-1]) * int(expression[i+1])
                    expression[i-1:i+2] = [temp]
                    i -= 1
                i += 1
        if abs(int(expression[0])) > answer:
            answer = abs(int(expression[0]))
        expression = copy.deepcopy(tp_expression)

    return answer
