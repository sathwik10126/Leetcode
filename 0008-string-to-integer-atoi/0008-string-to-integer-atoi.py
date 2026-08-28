class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        i = 0
        num = 0

        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num = num * sign

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num