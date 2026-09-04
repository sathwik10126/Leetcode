class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        ri=0
        st=""
        si=0
        while ri<len(s):
            while s[ri] in st:
                st=st[1:]
                l+=1
            st=st+s[ri]    
            si=max(si,len(st))
            ri+=1
        return si
        