class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1

        while start < end:
            sChar = s[start].lower()
            eChar = s[end].lower()

            # we could also use alnum() function for this
            if not (97 <= ord(sChar) <= 122) and not (48 <= ord(sChar) <= 57):
                print(sChar)
                start += 1
            elif not (97 <= ord(eChar) <= 122) and not (48 <= ord(eChar) <= 57):
                print(eChar)
                end -= 1
            else:
                if ord(sChar) != ord(eChar):
                    return False
                
                start += 1
                end -= 1
            
        return True