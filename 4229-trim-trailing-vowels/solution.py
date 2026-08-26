class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        while s and s[-1] in "aeiou":
            s=s[:-1]
        return s

        
