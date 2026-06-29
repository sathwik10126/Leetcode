class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        c=0

        x=word
        for i in patterns:
            if i in x:
                c+=+1
        return c

        
