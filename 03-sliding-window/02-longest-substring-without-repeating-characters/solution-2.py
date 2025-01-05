class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Doesn't use hash tables
        
        subst_count = 0
        maxSubst = 0
        subst = []

        for c in s:
            if c in subst:
                maxSubst = max(subst_count, maxSubst)
                
                index = subst.index(c)
                subst = subst[index+1:]

                subst.append(c)
                subst_count = len(subst)

            else:
                subst.append(c)
                subst_count += 1
        
        maxSubst = max(subst_count, maxSubst)
        return maxSubst
    