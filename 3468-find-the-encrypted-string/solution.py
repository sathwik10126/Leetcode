class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res=""
        for i in range(len(s)):
            res+=s[(i+k)%len(s)]
        return res
