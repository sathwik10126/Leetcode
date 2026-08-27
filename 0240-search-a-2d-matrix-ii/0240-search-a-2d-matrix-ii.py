class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        li=[]
        for i in matrix:
            for j in i:
                li.append(j)
        if target in li:
            return True
        else:
            return False
            
