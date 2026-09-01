class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=""
        words = s.split()
        for i in words:
            r+=i[::-1]+" "
        return r.strip()