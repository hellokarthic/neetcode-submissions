class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(int(a)+int(b))
                elif token == "-":
                    stack.append(int(a)-int(b))
                elif token == "*":
                    stack.append(int(a) * int(b))
                elif token == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
        