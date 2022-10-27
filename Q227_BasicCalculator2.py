class Solution:
    # stack
    def calculate(self, s: str) -> int:
        def cal(it):
            def update_stack(op, v):
                if op == "+":
                    stack.append(v)
                elif op == "-" :
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                elif op == "/":
                    stack.append(int(stack.pop() / v))
            num, stack, op = 0, [], '+'
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in '+-*/':
                    update_stack(op, num)  # update stack every time we encounter an operator; update with the lat operator, not the current one
                    num, op = 0, s[it]
                it += 1
            update_stack(op, num)
            return sum(stack)
        return cal(0)
