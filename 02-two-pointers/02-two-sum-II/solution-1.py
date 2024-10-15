class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = dict()

        for i, num in enumerate(numbers):
            second_num = target - num

            if second_num in hashMap:
                return [hashMap[second_num], i+1]
            else:
                hashMap[num] = i+1
            
        return -1
        