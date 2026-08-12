class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=""
        for i in str(n):
            if i!="0":
                x=x+i
        total = sum(map(int, str(x)))
        return int(x) * total if x.strip() and int(x) > 0 else 0
