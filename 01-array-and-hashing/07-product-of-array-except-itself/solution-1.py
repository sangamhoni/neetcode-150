'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(2n)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l2r = [1, nums[0]]
        r2l = [1, nums[-1]]

        for i in range(2, len(nums)):
            num = nums[i-1] * l2r[-1]
            l2r.append(num)
        
        for i in range(len(nums)-3, -1, -1):
            num = nums[i+1] * r2l[-1]
            r2l.append(num)

        result = []
        
        for i in range(len(l2r)):
            n1 = l2r[i]
            n2 = r2l[len(r2l)-i-1]
            result.append(n1*n2)
        
        return result
