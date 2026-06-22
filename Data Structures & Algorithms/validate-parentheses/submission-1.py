class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingToOpening = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in closingToOpening:
                if stack and stack[-1] == closingToOpening[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False