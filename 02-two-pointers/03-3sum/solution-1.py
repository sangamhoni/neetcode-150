class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []

        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue

            goal = 0 - num 
            l = i+1 
            r = len(nums) - 1

            while l<r:
                if nums[l] + nums[r] > goal:
                    r -= 1
                elif nums[l] + nums[r] < goal:
                    l += 1
                elif nums[l] + nums[r] == goal:

                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        
        return result
    