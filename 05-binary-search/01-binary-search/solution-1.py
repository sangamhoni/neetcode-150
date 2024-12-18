class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (r+l)//2
            # OR mid = l + (r-l)//2

            print(nums[mid])
            print(target)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        
        return -1
    