class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints) 
        s=0
        max_s = float('inf')

        l=0
        r=0
        if k == n:
            return total
        while r<n:
            s+=cardPoints[r]
            if r-l+1==n-k:
                max_s=min(s,max_s)
                s-=cardPoints[l]
                l+=1
            r+=1
        return total-max_s


