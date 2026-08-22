class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        p=1
        for i in str(n):
            s=s+int(i)
            p=p*int(i)

        if n%(s+p)==0:
            return(True)
        else:
            return(False)
        
