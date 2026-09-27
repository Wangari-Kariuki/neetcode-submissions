class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in closedToOpen:  # Closing bracket
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:                   # Opening bracket
                stack.append(c)

        return not stack
        