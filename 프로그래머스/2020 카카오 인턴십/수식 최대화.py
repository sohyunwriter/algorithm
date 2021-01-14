import itertools

def permute(nums):
    return list(itertools.permutations(nums))

def make_string2list(expression):
    expression_list = []
    operator = ['*', '+', '-']
    num = ""
    for i in expression:
        if i in operator:
            expression_list.append(int(num))
            num = ""
            expression_list.append(i)
        else:
            num += i
    expression_list.append(num)
    return expression_list

def make_postfix(expression, rank):
    postfix = []
    stack = []
    operator = ['*', '+', '-']
    for element in expression:
        if element in operator:
            while stack and rank[stack[-1]] >= rank[element]:
                postfix.append(stack.pop())
            stack.append(element)
            continue
        elif element == "(":
            stack.append(element)
            continue
        elif element == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
            continue
        postfix.append(element)

    while stack:
        postfix.append(stack.pop())

    return postfix

# postfix 연산
def eval_postfix(expression):
    stack = []
    for element in expression:
        if element == "+":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
        elif element == "-":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 - op2)
        elif element == "*":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 * op2)
        else:
            stack.append(int(element))
    return stack.pop()

def solution(expression):
    answer = 0
    ranklist = permute([1, 2, 3])
    orderlist = {"*": 0, "+": 0, "-": 0}
    expression_list = make_string2list(expression)
    for op1, op2, op3 in ranklist:
        orderlist["*"] = op1
        orderlist["+"] = op2
        orderlist["-"] = op3
        value = eval_postfix(make_postfix(expression_list, orderlist))
        if abs(value) >= answer:
            answer = abs(value)
    return answer


#print(make_string2list(["1", "*", "2", "+", "3"]))
#print(solution("100-200*300-500+20"))
#print(solution("50*6-3*2"))
