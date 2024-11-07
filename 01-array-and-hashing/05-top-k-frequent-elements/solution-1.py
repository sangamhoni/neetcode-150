class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rep = []
        num2rep = dict()

        for num in nums:
            if num in num2rep:
                num2rep[num] += 1
            else:
                num2rep[num] = 1

        rep = sorted(num2rep.values(), reverse=True)
        rep = rep[0:k]

        result = []

        for num in num2rep.copy():
            repet = num2rep[num]
            if repet in rep:
                result.append(num)
                del num2rep[num]

        return result
