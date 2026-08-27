class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l=[]
        for i in matrix:
            for j in i:
                l.append(j)
        l.sort()
        return(l[k-1])
        