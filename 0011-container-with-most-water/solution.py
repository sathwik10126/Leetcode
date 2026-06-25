class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        h=len(height)-1
        max_area=0
        while l<h:
            a=min(height[l],height[h])*(h-l)
            max_area=max(a,max_area)
            if height[l]<height[h]:
                l=l+1
            else:
                h=h-1
            
            
        return (max_area)
        
