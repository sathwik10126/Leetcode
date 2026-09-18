class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l=0
        r=0
        cost=0
        c=0
        while r<len(s):
            cost+=abs(ord(s[r])-ord(t[r]))
            while cost>maxCost:
                cost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            c=max(c,r-l+1)
            r+=1
        return c

        