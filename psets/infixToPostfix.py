from dspy.basic import Stack

def infixToPostfix(infixexpr):
    pred = {}
    pred["*"] = 3
    pred["/"] = 3
    pred["+"] = 2
    pred["-"] = 2
    pred["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
               (pred[opStack.peek()] >= pred[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

if __name__ == "__main__":
    print(infixToPostfix("( A + B ) * C"))
    print(infixToPostfix("A + B * C"))
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfix("1 + 2 * ( 3 + 4 )"))
