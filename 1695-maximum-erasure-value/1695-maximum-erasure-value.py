class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        s=0
        seen=set()
        ans=0
        while r<len(nums):
            if nums[r] not in seen:
                    seen.add(nums[r])
                    s += nums[r]
                    r += 1
                    ans = max(ans, s)
            else:
                seen.remove(nums[l])
                s -= nums[l]
                l += 1
        
        return ans