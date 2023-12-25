class Solution(object):
    def groupAnagrams(self, strs):
        # creating a hashmap to map all the anagrams
        result = defaultdict(list)
        
        for s in strs:
            # storing values a -> z
            count = [0] * 26 
            for c in s:
                # assigning the asci value to the count array
                count[ord(c) - ord("a")] += 1
            #appending all the s that contain the same count array
            #converting list to tuple as list cannot be keys
            result[tuple(count)].append(s)
        return result.values()
            