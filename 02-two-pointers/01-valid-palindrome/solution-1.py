class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        s = s.lower()
        
        while l<r:
            lChar = s[l]
            rChar = s[r]
            
            if not self.alnum(lChar):
                l += 1
            elif not self.alnum(rChar):
                r -= 1
            else:
                if lChar != rChar:
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True
    
    def alnum(self, a):
        # we could also use the inbuilt isalnum() method for this
        if 97 <= ord(a.lower()) <= 122 or 48 <= ord(a) <= 57:
            return True
        else:
            return False
