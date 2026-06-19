class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        temp=0
        result=[0]
        for i in gain:
            temp=temp+i
            result.append(temp)
        return max(result)     
