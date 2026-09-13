class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = 0
        r = 0
        s = []
        result = []
        while r < len(nums):
            s.append(nums[r])
            if r - l + 1 == k:
                s.sort()

                if k % 2 == 1:
                    median = s[k // 2]
                else:
                    median = (s[k // 2 - 1] + s[k // 2]) / 2.0
                result.append(median)
                s.remove(nums[l])
                l += 1
            r += 1
        return result
                

        
        