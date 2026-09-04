class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        curr_sum=sum(nums[:k])
        max_sum=curr_sum
        i=k
        while i<len(nums):
            curr_sum=curr_sum - nums[i-k] + nums[i]
            max_sum=max(max_sum,curr_sum)
            i+=1
        return float(max_sum)/k

        