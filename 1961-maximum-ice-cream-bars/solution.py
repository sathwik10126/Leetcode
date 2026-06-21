class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        co=sorted(costs)
        temp=0
        c=0
        for _ in range(len(co)):
            temp=temp+co[_]
            if(temp<=coins):
                c+=1
        return c
        
