class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=[]
        freq={}
        common=[]
        for i in strs:
            for j in range(1,len(i)+1):
                res.append(i[0:j])
                
        for i in res:
            freq[i]=freq.get(i,0)+1
            if(freq[i]==len(strs)):
                 common.append(i)
        return max(common, key=len) if common else ""




