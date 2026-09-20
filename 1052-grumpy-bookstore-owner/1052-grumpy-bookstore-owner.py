class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        total=0
        s=0
        max_s=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                total+=customers[i]
        l=0
        r=0
        while r<len(customers):
            if grumpy[r]==1:
                s+=customers[r]
            if r-l+1>minutes:
                if grumpy[l] == 1:
                    s-=customers[l]
                l+=1
            max_s=max(s,max_s)
            r+=1
        return total+max_s
        