class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in {'(',  '{', '['}:
                stack.append(char)
            else:
                if stack:
                    if char == ')' and stack.pop() != '(':
                        return False
                    if char == '}' and stack.pop() != '{':
                        return False
                    if char == ']' and stack.pop() != '[':
                        return False
                else:
                    return False
        
        return not stack