class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        r = ""

        nums = list(map(str, nums))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        for i in nums:
            r += i

        if r[0] == "0":
            return "0"

        return r

        