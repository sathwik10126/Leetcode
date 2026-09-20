class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        d=dict()
        i=0
        while i<26:
            d[chr(97+i)]=26-i
            i+=1
        for i,ch in enumerate(s,start=1):
            if ch in d:
                r+=i*d[ch]
        return r
        

