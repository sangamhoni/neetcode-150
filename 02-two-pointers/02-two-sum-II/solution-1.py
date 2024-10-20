class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(numbers)-1
        while l<r:
            sum = numbers[l] + numbers[r]

            print(sum)

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]


#  SOLUTION WITH O(N) TIME COMPLEXITY
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
        