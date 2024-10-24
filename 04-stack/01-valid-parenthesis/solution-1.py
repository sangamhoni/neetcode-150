class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {")": "(", "}": "{", "]": "["}
        brackets = []

        for b in s:
            if b in pair:
                if len(brackets) == 0 or brackets.pop() != pair[b]:
                    return False
            else:
                brackets.append(b)

        if len(brackets) != 0:
            return False

        return True
