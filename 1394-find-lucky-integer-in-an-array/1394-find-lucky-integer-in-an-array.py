class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        r=[]
        for i in range(len(arr)):
            if arr.count(arr[i])==arr[i]:
                r.append(arr[i])
        if len(r)==0:
            return -1
        else:
            return max(r)
        