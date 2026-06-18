class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=x=str(x)
        if(x==x[::-1]):
            return True
        else:
            return False


