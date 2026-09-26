class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        l=set(sentence)
        if len(l)==26:
            return True
        return False