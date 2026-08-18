from collections import Counter
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = Counter()

        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                count[x] += 1
        ans = [x for x in count if count[x] == 1]

        return max(ans) if ans else -1
