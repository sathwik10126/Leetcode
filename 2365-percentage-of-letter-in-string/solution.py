class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        
        x=s.count(letter)
        y=len(s)
        return ((x*100/y))
        
