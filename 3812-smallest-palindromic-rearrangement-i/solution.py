from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=""
        middle=""
        if len(s)==1:
            return s
        freq=Counter(s)
        for ch in sorted(freq):
            left += ch * (freq[ch] // 2)
            if freq[ch] % 2 == 1:
                middle = ch
        return left+middle+left[::-1]
        
            

        
        
