class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mySet = set()

        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        
        return False
