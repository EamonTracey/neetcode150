# You are given an array of strings tokens that represents
# an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents
# the value of the expression.
#
# Note that:
# 1. The valid operators are '+', '-', '*', and '/'.
# 2. Each operand may be an integer or another expression.
# 3. The division between two integers always truncates toward zero.
# 4. There will not be any division by zero.
# 5. The input represents a valid arithmetic expression in a reverse polish notation.
# 6. The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1 + op2)
            elif token == "-":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1 - op2)
            elif token == "*":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1 * op2)
            elif token == "/":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(token))
            
        return stack[0]
