class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
                ')': '(',
                ']': '[',
                '}': '{'
                }
        i = 0
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()

                


        return len(stack) == 0
