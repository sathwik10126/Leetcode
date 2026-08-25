class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=""
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        sorted_char = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
        for ch,count in sorted_char:
            r += ch *count

        return r

        
