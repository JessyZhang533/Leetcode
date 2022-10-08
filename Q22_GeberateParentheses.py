# Geberate Parentheses

def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):  # p: current string; left: number of unused left brackets; right: number of unused right right brackets
        if left:
            generate(p + '(', left-1, right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:  # !!!
            parens += p,
        return parens
    return generate('', n, n)
