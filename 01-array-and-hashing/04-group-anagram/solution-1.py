class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortStrs = []
        for word in strs:
            sortStrs.append("".join(sorted(word)))
        
        hashmap = dict()
        index = 0
        result = []

        for i, word in enumerate(strs):
            sortWord = sortStrs[i] 
            if sortWord in hashmap:
                result[hashmap[sortWord]].append(word)
            else:
                hashmap[sortWord] = index
                index += 1
                result.append([word])
        
        return result
