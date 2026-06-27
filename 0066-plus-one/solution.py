class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=""
        o=[]
        for num in digits:
            result+=str(num)
        res=int(result)+1
        for i in str(res):
            o.append(int(i))

        return o
