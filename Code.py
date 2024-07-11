class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                temp = ''
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()  # remove '('
                for char in temp:
                    stack.append(char)
            else:
                stack.append(c)
        return ''.join(stack)
