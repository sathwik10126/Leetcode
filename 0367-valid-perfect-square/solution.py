class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if((num**0.5)%1 !=0):
            return False
        else:
            return True
    
