import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        high=max(piles)
        ans=high
        while l<=high:
            m=(l+high)//2
            hours=sum(math.ceil(pile/float(m))for pile in piles)
            if hours<=h:
                ans=min(ans,m)
                high=m-1
            else:
                l=m+1
        return ans
