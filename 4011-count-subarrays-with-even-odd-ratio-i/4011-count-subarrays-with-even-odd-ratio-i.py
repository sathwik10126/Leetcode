class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        n=len(nums)
        c=0
        for i in range(n):
            x = 0
            y = 0
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    x += 1
                else:
                    y += 1
                if y > 0 and x * b <= a * y:
                    c+=1

        return c
            