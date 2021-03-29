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