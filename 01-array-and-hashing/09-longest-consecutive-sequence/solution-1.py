class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        seqNums = set()
        longestSeq = 0

        for num in nums:
            if num not in seqNums:
                seqNums.add(num)
                seqCount = 1

                start = num - 1 
                end = num + 1

                while start in nums:
                    seqNums.add(start)
                    seqCount += 1
                    start -= 1
                
                while end in nums:
                    seqNums.add(end)
                    seqCount += 1
                    end += 1
                
                longestSeq = max(longestSeq, seqCount)
    
        return longestSeq
