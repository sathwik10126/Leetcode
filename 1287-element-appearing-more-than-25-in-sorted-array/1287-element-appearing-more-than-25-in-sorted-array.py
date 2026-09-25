class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i in arr:
            if arr.count(i) > len(arr) * 0.25:
                return i
