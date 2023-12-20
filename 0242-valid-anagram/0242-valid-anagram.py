class Solution(object):
    def isAnagram(self, s, t):
        # sort the array and compare the two strings
        return sorted(s) == sorted(t)
        