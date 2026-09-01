class Solution:
    def isValid(self, strs: str) -> bool:
        if len(strs) % 2 != 0:
            return False

        stack = []
        group_brackets = {"(": ")", "{": "}", "[": "]"}

        for i, v in enumerate(strs):
            if v in group_brackets:
                stack.append(v)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if group_brackets[last] != v:
                    return False
        
        return len(stack) == 0