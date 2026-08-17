class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = sorted(list(set(nums)))
        nums[:len(k)] = k
        return len(k)
