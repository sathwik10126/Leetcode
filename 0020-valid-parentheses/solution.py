class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        match={")":"(","}":"{","]":"["}
        for ch in s:
            if ch in match:
                top=stack.pop() if len(stack)>0 else '_'
                if match[ch]!=top:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
                
            
