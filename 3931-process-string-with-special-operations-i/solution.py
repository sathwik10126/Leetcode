class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        for i in s:
            if(ord(i)>96 and ord(i)<123):
                result+=i
            elif(i=='*'):
                result=result[:-1]
            elif(i=='#'):
                result=result+result
            elif(i=='%'):
                result=result[::-1]
        return result
