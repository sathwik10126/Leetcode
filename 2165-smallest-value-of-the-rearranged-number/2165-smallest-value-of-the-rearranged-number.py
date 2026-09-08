class Solution(object):
    def smallestNumber(self, num):
        if num == 0:
            return 0

        negative = num < 0
        num = abs(num)

        l = []

        while num > 0:
            l.append(num % 10)
            num //= 10

        if negative:
            l.sort(reverse=True)
        else:
            l.sort()

            if l[0] == 0:
                for i in range(len(l)):
                    if l[i] != 0:
                        l[0], l[i] = l[i], l[0]
                        break

        r = ""

        for i in l:
            r += str(i)

        if negative:
            return -int(r)

        return int(r)