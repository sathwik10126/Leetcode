class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        res=s.split("|")
        for i in range(0, len(res),2):
            count+=res[i].count("*")
        return count
