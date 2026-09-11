class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        nums=set()
        from itertools import permutations
        for p in permutations(digits, 3):
            num = p[0] * 100 + p[1] * 10 + p[2]
            if p[0]!=0 and num%2==0:
                nums.add(num)
        return len(nums)

