class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        l,h=0,m*n-1
        while(l<=h):
            mid=(l+h)//2
            row=mid//n
            col=mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]<target:
                l=mid+1
            else:
                h=mid-1
        return False