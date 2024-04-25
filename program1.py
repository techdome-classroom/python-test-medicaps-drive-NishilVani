class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False
        if len(stack) == 0:
            return True
        return False
