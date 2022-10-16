# Valid Parentheses

# "()[]" true, "{()}" true, "{(})" false

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():  # stack is modified here (popped last item)
                    return False
            else:
                return False
        return stack == []
