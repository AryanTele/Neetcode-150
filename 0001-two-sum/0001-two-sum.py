class Solution(object):
    def twoSum(self, nums, target):
        # creating a hasmap for storing the index:value pair, empty initally
        hashMap = {}

        for i,n in enumerate(nums):
            #calculating the diff, checks if the diff exists in hashmap
            # if exist -> store(hashmap)
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        # if looped through all the elements return nothing
        return