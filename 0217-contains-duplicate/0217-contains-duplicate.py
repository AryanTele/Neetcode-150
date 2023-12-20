class Solution(object):
    def containsDuplicate(self, nums):
        #create a empty set
        seen = set()

        # loop through each element in nums
        for n in nums:
            # if n is in the set return ture
            if n in seen:
                return True
            # add n to the hashset if unique
            seen.add(n)
        #if n is not present in the set return false as each element is unique
        return False 
