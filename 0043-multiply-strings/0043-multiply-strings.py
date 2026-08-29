class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                result[i + j + 1] += a * b

        for i in range(len(result) - 1, 0, -1):
            result[i - 1] += result[i] // 10
            result[i] %= 10

        s = ""

        for x in result:
            if s != "" or x != 0:
                s += chr(x + ord('0'))

        return s