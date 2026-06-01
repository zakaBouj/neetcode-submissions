class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}

        for token in tokens:
            if token in op:
                num2 = stack.pop()
                num1 = stack.pop()

                match token:
                    case '+':
                        stack.append(num1 + num2)
                    case '-':
                        stack.append(num1 - num2)
                    case '*':
                        stack.append(num1 * num2)
                    case '/':
                        stack.append(int(num1 / num2))
            else:
                stack.append(int(token))

        return stack[0]