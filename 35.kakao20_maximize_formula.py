# 내 풀이
import re
from itertools import permutations

def greater_op_rank(op1, op2, op_rank):
    if op1 == op2:
        return True
    
    else:
        op1_rank = op_rank.index(op1)
        op2_rank = op_rank.index(op2)
        return op1_rank > op2_rank

def change(formula, op_rank):
    postfix_formula = []
    stack = []
    for i in formula:
        if type(i) is int:
            postfix_formula.append(i)
        else:
            if not stack:
                stack.append(i)
            else:
                while stack and greater_op_rank(stack[-1], i, op_rank):
                    postfix_formula.append(stack.pop())
                    
                stack.append(i)
                
    while stack:
        postfix_formula.append(stack.pop())

    return postfix_formula

def cal(formula):
    stack = []
    for i in formula:
        if type(i) is int:
            stack.append(i)
        else:
            if i == '-':
                stack.append(-stack.pop() + stack.pop())
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            else:
                stack.append(stack.pop() * stack.pop())
                
    return abs(stack.pop())

def solution(expression):
    formula = re.findall('[0-9]{1,3}|[-+*]', expression)
    formula = list(map(lambda x: int(x) if x.isdigit() else x, formula))
    op_rank_list = list(permutations(['+', '-', '*'], 3))
    
    answer = 0
    for op_rank in op_rank_list:
        postfix_formula = change(formula, op_rank)
        answer = max(cal(postfix_formula), answer)
    
    return answer

print(solution("100-200*300-500+20"))   # 60420
print(solution("50*6-3*2"))             # 300

# 다른 사람의 풀이 1
import re
from itertools import permutations

def solution1(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)

# 다른 사람의 풀이 2
from itertools import permutations
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution2(expression):
    answer = 0
    priorities = (list(permutations(['*','-','+'], 3)))
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer

# 다른 사람의 풀이 3
def solution3(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)