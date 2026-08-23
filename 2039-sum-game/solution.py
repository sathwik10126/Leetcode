class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        n1=num[0:(n//2)]
        n2=num[(n//2):n]
        q1=(n1.count('?'))
        q2=(n2.count('?'))
        s1=sum(int(i) for i in n1 if i.isdigit())
        s2=sum(int(i) for i in n2 if i.isdigit())
        return 2 * (s1 - s2) != 9 * (q2 - q1)

