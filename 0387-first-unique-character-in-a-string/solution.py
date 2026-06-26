class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for i in (s):
            freq[i]=freq.get(i,0)+1 

        for idx,i in enumerate(s):
            if(freq[i]==1):
                return idx
           
        return -1
