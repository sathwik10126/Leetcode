class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []

        l = 0

        while l < len(nums) - 2:
            m = l + 1
            r = len(nums) - 1

            while m < r:
                total = nums[l] + nums[m] + nums[r]

                if total == 0:
                    triplet = [nums[l], nums[m], nums[r]]

                    if triplet not in res:
                        res.append(triplet)

                    m += 1
                    r -= 1

                elif total < 0:
                    m += 1

                else:
                    r -= 1

            l += 1

        return res