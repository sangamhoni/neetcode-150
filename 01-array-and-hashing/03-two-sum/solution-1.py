class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict() 

        for i, num in enumerate(nums):
            search = target - num

            if search in map:
                return [map[search], i]
            else:
                map[num] = i
            
        return -1
