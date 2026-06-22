class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        r=""
        for i in s:
            if i.isalnum():
                r=r+i
        if(r==r[::-1]):
            return True
        else:
            return False
