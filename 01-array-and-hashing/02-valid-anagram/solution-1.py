class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # edge case: different character length
        if len(s) != len(t):
            return False
        
        hashS=dict()
        hashT=dict()

        for char1, char2 in zip(s, t):
            if char1 in hashS:
                hashS[char1] += 1
            else:
                hashS[char1] = 1

            if char2 in hashT:
                hashT[char2] += 1
            else:
                hashT[char2] = 1

        if len(hashS) != len(hashT):
            return False
        
        for char in hashS:
            if char not in hashT or hashS[char] != hashT[char]:
                return False
        
        return True
