class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if len(stack) == 0:
                    return False
                c2 = stack[-1]
                if c2 == "(" and c == ")":
                    stack.pop()
                elif c2 == "{" and c == "}":
                    stack.pop()
                elif c2 == "[" and c == "]":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False