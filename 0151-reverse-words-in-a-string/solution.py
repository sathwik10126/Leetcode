class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=s.split()[::-1]
        j=" ".join(x)
        return j
